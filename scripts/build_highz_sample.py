#!/usr/bin/env python3
"""
Phase 1: Build first z > 6 working sample from JADES DR5.

Downloads only FLAG + PHOTOZ extensions via HTTP range requests (~666 MB total),
then builds two samples:
  Sample A (wide):  z_peak > 6.0 with warning tags
  Sample B (clean): z_peak > 6.0, Prob_gt_6 >= 0.8, z_a >= 5.5, z_ml >= 5.5,
                    clean_longwave_nircam_bands >= 2, z_spec >= 5.5 if exists

Uses numpy for fast binary parsing instead of row-by-row struct.unpack.
"""
import urllib.request
import os
import csv
import json
import sys
import numpy as np
from datetime import datetime, timezone

BLOCK = 2880

CATALOGS = {
    "GOODS-S": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
    "GOODS-N": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
}

LONGWAVE_NIRCAM = {
    'F200W', 'F210M', 'F250M', 'F277W', 'F300M', 'F335M',
    'F356W', 'F410M', 'F430M', 'F444W', 'F460M', 'F480M'
}

FITS_TO_NUMPY = {
    'L': ('u1', 1),
    'B': ('u1', 1),
    'I': ('>i2', 2),
    'J': ('>i4', 4),
    'K': ('>i8', 8),
    'E': ('>f4', 4),
    'D': ('>f8', 8),
}


def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def fetch_range_chunked(url, start, total_bytes, chunk_size=8*1024*1024):
    pieces = []
    pos = start
    end = start + total_bytes - 1
    downloaded = 0
    while pos <= end:
        chunk_end = min(pos + chunk_size - 1, end)
        data = fetch_range(url, pos, chunk_end)
        pieces.append(data)
        downloaded += len(data)
        pct = downloaded / total_bytes * 100
        print(f"\r    {downloaded/(1024*1024):.0f}/{total_bytes/(1024*1024):.0f} MB ({pct:.0f}%)", end='', flush=True)
        pos = chunk_end + 1
    print()
    return b''.join(pieces)


def parse_header_at(url, offset):
    header_blocks = []
    pos = offset
    while pos - offset < 2_000_000:
        chunk_size = min(BLOCK * 40, 2_000_000 - (pos - offset))
        if chunk_size <= 0:
            break
        data = fetch_range(url, pos, pos + chunk_size - 1)
        found_end = False
        for b in range(0, len(data), BLOCK):
            block_data = data[b:b+BLOCK]
            if len(block_data) < BLOCK:
                block_data += b' ' * (BLOCK - len(block_data))
            text = block_data.decode('ascii', errors='replace')
            header_blocks.append(text)
            if any(text[j:j+80].startswith('END') for j in range(0, BLOCK, 80)):
                found_end = True
                break
        if found_end:
            break
        pos += chunk_size

    cards = {}
    for blk in header_blocks:
        for j in range(0, BLOCK, 80):
            line = blk[j:j+80]
            key = line[:8].strip()
            if key == 'END':
                break
            if '=' in line[:10] and key:
                cards[key] = line[10:].split('/')[0].strip().strip("'").strip()

    header_size = len(header_blocks) * BLOCK
    naxis1 = int(cards.get('NAXIS1', 0))
    naxis2 = int(cards.get('NAXIS2', 0))
    pcount = int(cards.get('PCOUNT', 0))
    naxis = int(cards.get('NAXIS', 0))
    data_size = (naxis1 * naxis2 + pcount) if naxis >= 2 else 0
    data_blocks = (data_size + BLOCK - 1) // BLOCK if data_size > 0 else 0

    columns = []
    ttype_keys = sorted([k for k in cards if k.startswith('TTYPE')], key=lambda k: int(k[5:]))
    for tk in ttype_keys:
        col_num = tk[5:]
        columns.append({
            'name': cards[tk],
            'format': cards.get(f'TFORM{col_num}', '?'),
        })

    return {
        'extname': cards.get('EXTNAME', ''),
        'naxis1': naxis1,
        'naxis2': naxis2,
        'tfields': int(cards.get('TFIELDS', 0)),
        'data_size': data_size,
        'header_size': header_size,
        'total_size': header_size + data_blocks * BLOCK,
        'columns': columns,
    }


def parse_format(fmt_str):
    if not fmt_str or fmt_str == '?':
        return None, None
    base = fmt_str[-1]
    repeat = int(fmt_str[:-1]) if len(fmt_str) > 1 else 1
    return base, repeat


def compute_column_layout(columns):
    layout = []
    offset = 0
    for col in columns:
        base, repeat = parse_format(col['format'])
        if base == 'A':
            size = repeat
            layout.append({'name': col['name'], 'base': base, 'repeat': repeat, 'offset': offset, 'size': size})
        elif base in FITS_TO_NUMPY:
            np_dtype, byte_size = FITS_TO_NUMPY[base]
            size = repeat * byte_size
            layout.append({'name': col['name'], 'base': base, 'repeat': repeat, 'offset': offset, 'size': size, 'dtype': np_dtype, 'byte_size': byte_size})
        else:
            raise ValueError(f"Unknown FITS format: {col['format']}")
        offset += size
    return layout, offset


def extract_columns_numpy(raw_data, row_size, nrows, column_layout, needed_names):
    result = {}
    for cl in column_layout:
        if cl['name'] not in needed_names:
            continue
        if cl['base'] == 'A':
            continue
        if cl['repeat'] != 1:
            continue

        col_data = np.zeros(nrows, dtype=np.float64)
        byte_size = cl['byte_size']
        col_offset = cl['offset']

        buf = np.frombuffer(raw_data, dtype='u1')
        indices = np.arange(nrows) * row_size + col_offset

        if cl['base'] == 'D':
            for i in range(nrows):
                start = i * row_size + col_offset
                col_data[i] = np.frombuffer(raw_data[start:start+8], dtype='>f8')[0]
        elif cl['base'] == 'E':
            for i in range(nrows):
                start = i * row_size + col_offset
                col_data[i] = np.frombuffer(raw_data[start:start+4], dtype='>f4')[0]
        elif cl['base'] == 'K':
            for i in range(nrows):
                start = i * row_size + col_offset
                col_data[i] = np.frombuffer(raw_data[start:start+8], dtype='>i8')[0]
        elif cl['base'] == 'J':
            for i in range(nrows):
                start = i * row_size + col_offset
                col_data[i] = np.frombuffer(raw_data[start:start+4], dtype='>i4')[0]

        result[cl['name']] = col_data

    return result


def extract_columns_fast(raw_data, row_size, nrows, column_layout, needed_names):
    result = {}
    raw_arr = np.frombuffer(raw_data, dtype='u1')

    for cl in column_layout:
        if cl['name'] not in needed_names:
            continue
        if cl['base'] == 'A' or cl['repeat'] != 1:
            continue

        byte_size = cl['byte_size']
        col_offset = cl['offset']
        dtype_str = cl['dtype']

        col_bytes = np.lib.stride_tricks.as_strided(
            raw_arr[col_offset:],
            shape=(nrows, byte_size),
            strides=(row_size, 1)
        ).copy()

        col_data = np.frombuffer(col_bytes.tobytes(), dtype=dtype_str)
        result[cl['name']] = col_data.astype(np.float64)

    return result


def scan_extensions(url):
    print(f"  Scanning headers...")
    file_size_req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(file_size_req, timeout=30) as resp:
        file_size = int(resp.headers.get('Content-Length', 0))

    offset = 0
    extensions = []
    ext_num = 0
    while offset < file_size:
        ext_info = parse_header_at(url, offset)
        ext_info['data_offset'] = offset + ext_info['header_size']
        ext_info['ext_num'] = ext_num
        extname = ext_info['extname'] or 'PRIMARY'
        print(f"    Ext {ext_num}: {extname:20s} @ {offset:>15,}")
        offset += ext_info['total_size']
        ext_num += 1
        extensions.append(ext_info)

    return extensions, file_size


def process_field(field_name, url):
    print(f"\n{'='*60}")
    print(f"  {field_name}")
    print(f"{'='*60}")

    extensions, _ = scan_extensions(url)

    flag_ext = next((e for e in extensions if e['extname'] == 'FLAG'), None)
    photoz_ext = next((e for e in extensions if e['extname'] == 'PHOTOZ'), None)

    if not flag_ext or not photoz_ext:
        print(f"  ERROR: Missing FLAG or PHOTOZ")
        return [], []

    flag_layout, flag_row_size = compute_column_layout(flag_ext['columns'])
    photoz_layout, photoz_row_size = compute_column_layout(photoz_ext['columns'])

    lw_flag_cols = [cl['name'] for cl in flag_layout
                    if cl['name'].endswith('_FLAG') and cl['name'].replace('_FLAG', '') in LONGWAVE_NIRCAM]
    print(f"  Long-wave FLAG columns ({len(lw_flag_cols)}): {lw_flag_cols}")

    needed_flag = {'ID', 'RA', 'DEC'} | set(lw_flag_cols)
    needed_photoz = {'ID', 'z_spec', 'z_a', 'z_ml', 'chi_a', 'z_peak', 'chi_peak', 'nfilt',
                     'Prob_gt_5', 'Prob_gt_6', 'Prob_gt_7', 'Prob_gt_8', 'Prob_gt_9',
                     'chisq_z_lt_4', 'chisq_z_lt_5', 'chisq_z_lt_6', 'chisq_z_lt_7'}

    nrows = photoz_ext['naxis2']

    print(f"\n  Downloading PHOTOZ ({photoz_ext['data_size']/(1024*1024):.0f} MB)...")
    photoz_raw = fetch_range_chunked(url, photoz_ext['data_offset'], photoz_ext['data_size'])
    print(f"  Parsing PHOTOZ columns (numpy)...")
    pz = extract_columns_fast(photoz_raw, photoz_row_size, nrows, photoz_layout, needed_photoz)
    del photoz_raw

    z_peak = pz['z_peak']
    mask_a = z_peak > 6.0
    n_candidates = np.sum(mask_a)
    print(f"  z_peak > 6.0: {n_candidates:,} / {nrows:,} sources ({n_candidates/nrows*100:.1f}%)")

    print(f"\n  Downloading FLAG ({flag_ext['data_size']/(1024*1024):.0f} MB)...")
    flag_raw = fetch_range_chunked(url, flag_ext['data_offset'], flag_ext['data_size'])
    print(f"  Parsing FLAG columns (numpy)...")
    fl = extract_columns_fast(flag_raw, flag_row_size, nrows, flag_layout, needed_flag)
    del flag_raw

    print(f"\n  Building samples...")

    z_a = pz['z_a']
    z_ml = pz['z_ml']
    z_spec = pz['z_spec']
    prob_gt_6 = pz['Prob_gt_6']
    prob_gt_7 = pz['Prob_gt_7']
    prob_gt_8 = pz['Prob_gt_8']
    prob_gt_9 = pz['Prob_gt_9']
    chi_a = pz['chi_a']
    nfilt = pz['nfilt']
    chisq_z_lt_4 = pz.get('chisq_z_lt_4', np.zeros(nrows))

    clean_lw_count = np.zeros(nrows, dtype=np.int32)
    for col_name in lw_flag_cols:
        flag_vals = fl[col_name]
        clean_lw_count += (flag_vals == 0).astype(np.int32)

    tag_low_prob = (prob_gt_6 < 0.5).astype(np.int32)
    tag_spec_conflict = ((z_spec > 0) & (z_spec < 5.5)).astype(np.int32)
    tag_low_red_coverage = (clean_lw_count < 2).astype(np.int32)

    tag_lowz_competitive = np.zeros(nrows, dtype=np.int32)
    valid_chi = (chi_a > 0) & (chisq_z_lt_4 > 0) & np.isfinite(chi_a) & np.isfinite(chisq_z_lt_4)
    ratio = np.where(valid_chi, chisq_z_lt_4 / chi_a, 999.0)
    tag_lowz_competitive[ratio < 2.0] = 1

    idx_a = np.where(mask_a)[0]

    mask_b = (mask_a &
              (prob_gt_6 >= 0.8) &
              (z_a >= 5.5) &
              (z_ml >= 5.5) &
              (clean_lw_count >= 2) &
              ~((z_spec > 0) & (z_spec < 5.5)))
    idx_b = np.where(mask_b)[0]

    print(f"  Sample A (wide):  {len(idx_a):,}")
    print(f"  Sample B (clean): {len(idx_b):,}")

    def build_rows(indices):
        rows = []
        for i in indices:
            rows.append({
                'field': field_name,
                'ID': int(fl['ID'][i]),
                'RA': float(fl['RA'][i]),
                'DEC': float(fl['DEC'][i]),
                'z_peak': float(z_peak[i]),
                'z_a': float(z_a[i]),
                'z_ml': float(z_ml[i]),
                'z_spec': float(z_spec[i]),
                'Prob_gt_6': float(prob_gt_6[i]),
                'Prob_gt_7': float(prob_gt_7[i]),
                'Prob_gt_8': float(prob_gt_8[i]),
                'Prob_gt_9': float(prob_gt_9[i]),
                'chi_a': float(chi_a[i]),
                'nfilt': int(nfilt[i]),
                'clean_lw_bands': int(clean_lw_count[i]),
                'tag_low_prob': int(tag_low_prob[i]),
                'tag_spec_conflict': int(tag_spec_conflict[i]),
                'tag_low_red_coverage': int(tag_low_red_coverage[i]),
                'tag_lowz_competitive': int(tag_lowz_competitive[i]),
            })
        return rows

    sample_a = build_rows(idx_a)
    sample_b = build_rows(idx_b)

    return sample_a, sample_b


def print_distribution(z_vals, label):
    if not z_vals:
        return
    z_arr = np.array(z_vals)
    print(f"\n  --- {label} z_peak distribution ---")
    bins = [(6, 7), (7, 8), (8, 9), (9, 10), (10, 12), (12, 15), (15, 30)]
    for lo, hi in bins:
        count = int(np.sum((z_arr >= lo) & (z_arr < hi)))
        if count > 0:
            bar = '#' * min(count // max(len(z_vals)//500, 1), 50)
            print(f"    z = {lo:>2}-{hi:<2}: {count:>6,}  {bar}")
    print(f"    median: {float(np.median(z_arr)):.2f}")
    print(f"    max:    {float(np.max(z_arr)):.2f}")


def save_csv(records, filepath):
    if not records:
        return
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    keys = list(records[0].keys())
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)
    print(f"  Saved {len(records):,} rows -> {filepath}")


def main():
    print("="*60)
    print("  JADES DR5 — Phase 1: Build z > 6 Sample")
    print(f"  {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*60)

    all_a = []
    all_b = []

    for field_name, url in CATALOGS.items():
        sa, sb = process_field(field_name, url)
        all_a.extend(sa)
        all_b.extend(sb)

    save_csv(all_a, "data/research/sample_a_wide.csv")
    save_csv(all_b, "data/research/sample_b_clean.csv")

    print(f"\n\n{'='*60}")
    print(f"  COMBINED RESULTS")
    print(f"{'='*60}")
    print(f"\n  Total Sample A (wide):  {len(all_a):,}")
    print(f"  Total Sample B (clean): {len(all_b):,}")

    z_a_vals = [r['z_peak'] for r in all_a]
    z_b_vals = [r['z_peak'] for r in all_b]

    print_distribution(z_a_vals, "Sample A (wide)")
    print_distribution(z_b_vals, "Sample B (clean)")

    if all_a:
        print(f"\n  --- Sample A warning tags ---")
        tags = ['tag_low_prob', 'tag_spec_conflict', 'tag_low_red_coverage', 'tag_lowz_competitive']
        for tag in tags:
            count = sum(1 for r in all_a if r[tag] == 1)
            pct = count / len(all_a) * 100
            print(f"    {tag}: {count:>6,} / {len(all_a):,} ({pct:.1f}%)")

        per_field = {}
        for r in all_a:
            f = r['field']
            if f not in per_field:
                per_field[f] = {'a': 0, 'b': 0}
            per_field[f]['a'] += 1
        for r in all_b:
            f = r['field']
            per_field[f]['b'] += 1

        print(f"\n  --- Per-field breakdown ---")
        for f, counts in per_field.items():
            print(f"    {f}: A={counts['a']:,}, B={counts['b']:,}")

    print(f"\n  Phase 1 complete.")


if __name__ == '__main__':
    main()
