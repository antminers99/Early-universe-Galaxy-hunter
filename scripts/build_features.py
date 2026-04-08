#!/usr/bin/env python3
"""
Phase 3A: Pull photometry + size features for the 7,954 sources in sample_b_killed_v1.
Downloads KRON + SIZE extensions, extracts flux/error/size columns, builds features table.
"""
import urllib.request
import csv
import os
import sys
import numpy as np
from datetime import datetime, timezone

BLOCK = 2880

CATALOGS = {
    "GOODS-S": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
    "GOODS-N": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
}

TARGET_BANDS = ['F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']

FITS_TO_NUMPY = {
    'L': ('u1', 1), 'B': ('u1', 1), 'I': ('>i2', 2),
    'J': ('>i4', 4), 'K': ('>i8', 8), 'E': ('>f4', 4), 'D': ('>f8', 8),
}


def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def fetch_chunked(url, start, total, chunk=16*1024*1024):
    pieces = []
    pos = start
    end = start + total - 1
    dl = 0
    while pos <= end:
        ce = min(pos + chunk - 1, end)
        pieces.append(fetch_range(url, pos, ce))
        dl += len(pieces[-1])
        print(f"\r    {dl/(1024*1024):.0f}/{total/(1024*1024):.0f} MB", end='', flush=True)
        pos = ce + 1
    print()
    return b''.join(pieces)


def parse_header(url, offset):
    blocks = []
    pos = offset
    while pos - offset < 2_000_000:
        sz = min(BLOCK * 40, 2_000_000 - (pos - offset))
        if sz <= 0:
            break
        data = fetch_range(url, pos, pos + sz - 1)
        done = False
        for b in range(0, len(data), BLOCK):
            bd = data[b:b+BLOCK]
            if len(bd) < BLOCK:
                bd += b' ' * (BLOCK - len(bd))
            txt = bd.decode('ascii', errors='replace')
            blocks.append(txt)
            if any(txt[j:j+80].startswith('END') for j in range(0, BLOCK, 80)):
                done = True
                break
        if done:
            break
        pos += sz

    cards = {}
    for blk in blocks:
        for j in range(0, BLOCK, 80):
            line = blk[j:j+80]
            key = line[:8].strip()
            if key == 'END':
                break
            if '=' in line[:10] and key:
                cards[key] = line[10:].split('/')[0].strip().strip("'").strip()

    hs = len(blocks) * BLOCK
    n1 = int(cards.get('NAXIS1', 0))
    n2 = int(cards.get('NAXIS2', 0))
    pc = int(cards.get('PCOUNT', 0))
    na = int(cards.get('NAXIS', 0))
    ds = (n1 * n2 + pc) if na >= 2 else 0
    db = (ds + BLOCK - 1) // BLOCK if ds > 0 else 0

    cols = []
    tkeys = sorted([k for k in cards if k.startswith('TTYPE')], key=lambda k: int(k[5:]))
    for tk in tkeys:
        cn = tk[5:]
        cols.append({'name': cards[tk], 'format': cards.get(f'TFORM{cn}', '?')})

    return {
        'extname': cards.get('EXTNAME', ''),
        'naxis1': n1, 'naxis2': n2,
        'data_size': ds, 'header_size': hs,
        'total_size': hs + db * BLOCK,
        'data_offset': offset + hs,
        'columns': cols,
    }


def compute_layout(columns):
    layout = []
    offset = 0
    for col in columns:
        fmt = col['format']
        base = fmt[-1] if fmt else '?'
        repeat = int(fmt[:-1]) if len(fmt) > 1 else 1
        if base == 'A':
            size = repeat
            layout.append({'name': col['name'], 'base': 'A', 'repeat': repeat,
                          'offset': offset, 'size': size})
        elif base in FITS_TO_NUMPY:
            dt, bs = FITS_TO_NUMPY[base]
            size = repeat * bs
            layout.append({'name': col['name'], 'base': base, 'repeat': repeat,
                          'offset': offset, 'size': size, 'dtype': dt, 'byte_size': bs})
        else:
            raise ValueError(f"Unknown: {fmt}")
        offset += size
    return layout, offset


def extract_cols(raw, row_size, nrows, layout, names):
    result = {}
    raw_arr = np.frombuffer(raw, dtype='u1')
    for cl in layout:
        if cl['name'] not in names or cl['base'] == 'A' or cl['repeat'] != 1:
            continue
        bs = cl['byte_size']
        co = cl['offset']
        col_bytes = np.lib.stride_tricks.as_strided(
            raw_arr[co:], shape=(nrows, bs), strides=(row_size, 1)
        ).copy()
        result[cl['name']] = np.frombuffer(col_bytes.tobytes(), dtype=cl['dtype']).astype(np.float64)
    return result


def scan_exts(url):
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req, timeout=30) as resp:
        fsz = int(resp.headers.get('Content-Length', 0))
    off = 0
    exts = {}
    while off < fsz:
        e = parse_header(url, off)
        exts[e['extname'] or 'PRIMARY'] = e
        off += e['total_size']
    return exts


def process_field(field, url, sample_ids):
    print(f"\n{'='*60}")
    print(f"  {field} — scanning extensions")
    print(f"{'='*60}")

    exts = scan_exts(url)
    kron_ext = exts['KRON']
    size_ext = exts['SIZE']
    nrows = kron_ext['naxis2']

    kron_layout, kron_rs = compute_layout(kron_ext['columns'])
    size_layout, size_rs = compute_layout(size_ext['columns'])

    needed_kron = {'ID'}
    for b in TARGET_BANDS:
        needed_kron.add(f'{b}_KRON')
        needed_kron.add(f'{b}_KRON_e')

    needed_size = {'ID', 'A', 'B', 'R_KRON_U', 'FWHM', 'GINI'}

    print(f"  Downloading KRON ({kron_ext['data_size']/(1024*1024):.0f} MB)...")
    kron_raw = fetch_chunked(url, kron_ext['data_offset'], kron_ext['data_size'])
    print(f"  Parsing KRON columns...")
    kron_data = extract_cols(kron_raw, kron_rs, nrows, kron_layout, needed_kron)
    del kron_raw

    print(f"  Downloading SIZE ({size_ext['data_size']/(1024*1024):.0f} MB)...")
    size_raw = fetch_chunked(url, size_ext['data_offset'], size_ext['data_size'])
    print(f"  Parsing SIZE columns...")
    size_data = extract_cols(size_raw, size_rs, nrows, size_layout, needed_size)
    del size_raw

    all_ids = kron_data['ID'].astype(np.int64)
    id_to_idx = {}
    for i in range(nrows):
        id_val = int(all_ids[i])
        if id_val in sample_ids:
            id_to_idx[id_val] = i

    print(f"  Matched {len(id_to_idx):,} / {len(sample_ids):,} sample IDs")

    results = {}
    for src_id, row_idx in id_to_idx.items():
        feat = {}
        for b in TARGET_BANDS:
            fname = f'{b}_KRON'
            ename = f'{b}_KRON_e'
            feat[f'{b}_flux'] = float(kron_data[fname][row_idx])
            feat[f'{b}_err'] = float(kron_data[ename][row_idx])
        feat['A'] = float(size_data['A'][row_idx])
        feat['B'] = float(size_data['B'][row_idx])
        feat['R_KRON_U'] = float(size_data['R_KRON_U'][row_idx])
        feat['FWHM'] = float(size_data['FWHM'][row_idx])
        feat['GINI'] = float(size_data['GINI'][row_idx])
        results[src_id] = feat

    return results


def main():
    print("="*60)
    print("  Phase 3A: Pull Features for sample_b_killed_v1")
    print(f"  {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*60)

    with open('data/research/sample_b_killed_v1.csv') as f:
        sample = list(csv.DictReader(f))
    print(f"  Loaded {len(sample):,} sources from sample_b_killed_v1.csv")

    ids_by_field = {}
    for r in sample:
        fld = r['field']
        sid = int(r['ID'])
        if fld not in ids_by_field:
            ids_by_field[fld] = set()
        ids_by_field[fld].add(sid)

    for fld, ids in ids_by_field.items():
        print(f"  {fld}: {len(ids):,} sources")

    all_features = {}

    for field, url in CATALOGS.items():
        if field not in ids_by_field:
            continue
        feats = process_field(field, url, ids_by_field[field])
        all_features.update({(field, sid): feat for sid, feat in feats.items()})
        np_cache_path = f'data/research/.features_cache_{field.lower().replace("-","_")}.npz'
        np.savez_compressed(np_cache_path,
            ids=np.array(list(feats.keys())),
            **{k: np.array([feats[sid][k] for sid in feats]) for k in list(feats.values())[0].keys()})
        print(f"  Cached {field} features to {np_cache_path}")

    out_rows = []
    for r in sample:
        fld = r['field']
        sid = int(r['ID'])
        key = (fld, sid)
        if key not in all_features:
            continue

        feat = all_features[key]
        z_peak = float(r['z_peak'])

        if z_peak < 8:
            bin_z = '6-8'
        elif z_peak < 10:
            bin_z = '8-10'
        else:
            bin_z = '10-15'

        clean_bands = 0
        for b in TARGET_BANDS:
            flux = feat[f'{b}_flux']
            err = feat[f'{b}_err']
            if np.isfinite(flux) and np.isfinite(err) and err > 0 and flux != 0:
                clean_bands += 1

        f444w_snr = 0
        if np.isfinite(feat['F444W_err']) and feat['F444W_err'] > 0:
            f444w_snr = feat['F444W_flux'] / feat['F444W_err']
        f356w_snr = 0
        if np.isfinite(feat['F356W_err']) and feat['F356W_err'] > 0:
            f356w_snr = feat['F356W_flux'] / feat['F356W_err']

        size_a = feat['A']
        size_usable = 1 if (np.isfinite(size_a) and size_a > 0) else 0

        row = {
            'field': fld,
            'ID': r['ID'],
            'RA': r['RA'],
            'DEC': r['DEC'],
            'z_peak': r['z_peak'],
            'z_a': r['z_a'],
            'z_ml': r['z_ml'],
            'Prob_gt_6': r['Prob_gt_6'],
            'bin_z': bin_z,
        }

        for b in TARGET_BANDS:
            row[f'{b}_flux'] = f"{feat[f'{b}_flux']:.4f}"
            row[f'{b}_err'] = f"{feat[f'{b}_err']:.4f}"

        row['A_arcsec'] = f"{feat['A']:.4f}"
        row['B_arcsec'] = f"{feat['B']:.4f}"
        row['R_KRON_U'] = f"{feat['R_KRON_U']:.4f}"
        row['FWHM_arcsec'] = f"{feat['FWHM']:.4f}"
        row['GINI'] = f"{feat['GINI']:.4f}"
        row['clean_phot_bands'] = clean_bands
        row['size_usable'] = size_usable
        row['F444W_SNR'] = f"{f444w_snr:.2f}"
        row['F356W_SNR'] = f"{f356w_snr:.2f}"

        out_rows.append(row)

    os.makedirs('data/research', exist_ok=True)
    out_path = 'data/research/sample_b_features_v1.csv'
    if out_rows:
        keys = list(out_rows[0].keys())
        with open(out_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(out_rows)
    print(f"\n  Saved {len(out_rows):,} rows -> {out_path}")

    print(f"\n{'='*60}")
    print(f"  Phase 3A + 3B SUMMARY")
    print(f"{'='*60}")

    bins = ['6-8', '8-10', '10-15']
    print(f"\n  Sources per bin:")
    for bz in bins:
        n = sum(1 for r in out_rows if r['bin_z'] == bz)
        print(f"    bin {bz}: {n:,}")

    print(f"\n  Photometry coverage (clean bands with finite flux+error):")
    for bz in bins:
        br = [r for r in out_rows if r['bin_z'] == bz]
        if not br:
            continue
        avg_clean = np.mean([r['clean_phot_bands'] for r in br])
        has_5plus = sum(1 for r in br if r['clean_phot_bands'] >= 5)
        print(f"    bin {bz}: avg clean bands = {avg_clean:.1f}, >=5 bands = {has_5plus:,}/{len(br):,} ({has_5plus/len(br)*100:.0f}%)")

    print(f"\n  Size usability:")
    for bz in bins:
        br = [r for r in out_rows if r['bin_z'] == bz]
        if not br:
            continue
        usable = sum(1 for r in br if r['size_usable'] == 1)
        print(f"    bin {bz}: size usable = {usable:,}/{len(br):,} ({usable/len(br)*100:.0f}%)")

    print(f"\n  Reference band comparison (SNR > 3):")
    for bz in bins:
        br = [r for r in out_rows if r['bin_z'] == bz]
        if not br:
            continue
        f444_good = sum(1 for r in br if float(r['F444W_SNR']) > 3)
        f356_good = sum(1 for r in br if float(r['F356W_SNR']) > 3)
        print(f"    bin {bz}: F444W SNR>3 = {f444_good:,}/{len(br):,} ({f444_good/len(br)*100:.0f}%)  |  F356W SNR>3 = {f356_good:,}/{len(br):,} ({f356_good/len(br)*100:.0f}%)")

    best = 'F444W' if sum(1 for r in out_rows if float(r['F444W_SNR']) > 3) >= sum(1 for r in out_rows if float(r['F356W_SNR']) > 3) else 'F356W'
    print(f"\n  >>> Recommended reference band: {best}")

    print(f"\n  Phase 3A complete.")


if __name__ == '__main__':
    main()
