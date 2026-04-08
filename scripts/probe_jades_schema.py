#!/usr/bin/env python3
"""
Probe JADES DR5 catalog schema via HTTP range requests.
Reads only FITS headers (~5 MB total) — does NOT download the full files.
Outputs a full schema report for both GOODS-S and GOODS-N.
"""
import urllib.request
import json
import sys
import os
from datetime import datetime

BLOCK = 2880

CATALOGS = {
    "GOODS-S": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
    "GOODS-N": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
}

FITS_FORMAT_NAMES = {
    'L': 'logical',
    'B': 'unsigned byte',
    'I': 'int16',
    'J': 'int32',
    'K': 'int64',
    'E': 'float32',
    'D': 'float64',
    'C': 'complex64',
    'M': 'complex128',
    'A': 'char',
    'P': 'var-length (32-bit)',
    'Q': 'var-length (64-bit)',
}

def get_file_size(url):
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req, timeout=30) as resp:
        return int(resp.headers.get('Content-Length', 0))

def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()

def parse_header_at(url, offset):
    header_blocks = []
    pos = offset
    max_header_read = 2_000_000
    while pos - offset < max_header_read:
        chunk_size = min(BLOCK * 40, max_header_read - (pos - offset))
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
            lines = [text[j:j+80] for j in range(0, BLOCK, 80)]
            if any(l.startswith('END') for l in lines):
                found_end = True
                break
        if found_end:
            break
        pos += chunk_size

    cards = {}
    ordered_keys = []
    for blk in header_blocks:
        for j in range(0, BLOCK, 80):
            line = blk[j:j+80]
            key = line[:8].strip()
            if key == 'END':
                break
            if '=' in line[:10] and key:
                val = line[10:].split('/')[0].strip().strip("'").strip()
                cards[key] = val
                ordered_keys.append(key)

    header_size = len(header_blocks) * BLOCK
    naxis = int(cards.get('NAXIS', 0))
    naxis1 = int(cards.get('NAXIS1', 0))
    naxis2 = int(cards.get('NAXIS2', 0))
    pcount = int(cards.get('PCOUNT', 0))
    tfields = int(cards.get('TFIELDS', 0))

    if naxis >= 2:
        data_size = naxis1 * naxis2 + pcount
    else:
        data_size = 0

    data_blocks = (data_size + BLOCK - 1) // BLOCK if data_size > 0 else 0
    total_size = header_size + data_blocks * BLOCK

    columns = []
    ttype_keys = sorted([k for k in cards if k.startswith('TTYPE')], key=lambda k: int(k[5:]))
    tform_keys = {f'TFORM{k[5:]}': cards.get(f'TFORM{k[5:]}', '') for k in ttype_keys}

    for tk in ttype_keys:
        col_num = tk[5:]
        col_name = cards[tk]
        col_format = cards.get(f'TFORM{col_num}', '?')
        col_unit = cards.get(f'TUNIT{col_num}', '')
        columns.append({
            'name': col_name,
            'format': col_format,
            'unit': col_unit,
        })

    return {
        'extname': cards.get('EXTNAME', ''),
        'xtension': cards.get('XTENSION', cards.get('SIMPLE', '')),
        'naxis1': naxis1,
        'naxis2': naxis2,
        'tfields': tfields,
        'pcount': pcount,
        'data_size': data_size,
        'total_size': total_size,
        'columns': columns,
        'cards': cards,
    }, total_size

def scan_all_extensions(field, url, file_size):
    print(f"\n{'='*70}")
    print(f"  {field}")
    print(f"  URL: {url}")
    print(f"  Verified file size: {file_size:,} bytes ({file_size/1e9:.2f} GB)")
    print(f"{'='*70}")

    offset = 0
    ext_num = 0
    extensions = []
    total_bytes_read = 0

    while offset < file_size:
        ext, size = parse_header_at(url, offset)
        extname = ext['extname'] or 'PRIMARY'
        data_mb = ext['data_size'] / 1e6

        print(f"\n  Ext {ext_num}: {extname:20s} | rows={ext['naxis2']:>8,} | cols={ext['tfields']:>4} | data={data_mb:>8.1f} MB")

        ext['ext_num'] = ext_num
        ext['extname'] = extname
        extensions.append(ext)

        offset += size
        ext_num += 1
        total_bytes_read += len(ext.get('columns', [])) * 80 + BLOCK * 2

    print(f"\n  Total extensions: {ext_num}")
    print(f"  Approximate header bytes read: ~{total_bytes_read / 1024:.0f} KB (no data downloaded)")
    return extensions

def format_column_table(columns):
    lines = []
    lines.append(f"| {'#':>3} | {'Column Name':<30} | {'Format':<12} | {'Type':<20} | {'Unit':<10} |")
    lines.append(f"|{'---':>5}|{'-'*32}|{'-'*14}|{'-'*22}|{'-'*12}|")
    for i, col in enumerate(columns):
        fmt_raw = col['format']
        repeat = ''
        base_type = fmt_raw[-1] if fmt_raw else '?'
        if len(fmt_raw) > 1:
            repeat = fmt_raw[:-1]
        type_name = FITS_FORMAT_NAMES.get(base_type, fmt_raw)
        if repeat and repeat != '1':
            type_name = f"{type_name}[{repeat}]"
        lines.append(f"| {i+1:>3} | {col['name']:<30} | {fmt_raw:<12} | {type_name:<20} | {col['unit']:<10} |")
    return '\n'.join(lines)

def check_research_columns(extensions):
    needed = {
        'photo-z (EAZY)': False,
        'spectroscopic z': False,
        'RA/Dec coordinates': False,
        'quality flags': False,
        'NIRCam photometry (F090W-F444W)': False,
        'effective radius (R_eff)': False,
        'Kron photometry': False,
        'MIRI photometry': False,
    }

    for ext in extensions:
        for col in ext['columns']:
            cn = col['name'].upper()
            if 'Z_PEAK' in cn or 'Z_A' == cn or 'Z_ML' in cn or cn.startswith('Z_') and 'CHISQ' not in cn:
                needed['photo-z (EAZY)'] = True
            if 'Z_SPEC' in cn:
                needed['spectroscopic z'] = True
            if cn in ('RA', 'DEC'):
                needed['RA/Dec coordinates'] = True
            if 'FLAG' in cn:
                needed['quality flags'] = True
            if any(f in cn for f in ['F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']):
                needed['NIRCam photometry (F090W-F444W)'] = True
            if 'KRON' in cn:
                needed['Kron photometry'] = True
            if cn.startswith('F770W') or cn.startswith('F1000W') or cn.startswith('F1280W'):
                needed['MIRI photometry'] = True
            if 'R_EFF' in cn or 'REFF' in cn or ('A' == cn and ext['extname'] == 'SIZE') or ('B' == cn and ext['extname'] == 'SIZE'):
                needed['effective radius (R_eff)'] = True

    return needed

def generate_report(all_results):
    lines = []
    lines.append("# JADES DR5 Catalog Schema Report")
    lines.append(f"\n**Generated:** {datetime.now(tz=__import__('datetime').timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append("**Method:** HTTP range requests (header-only, no full file download)")
    lines.append("")

    for field, info in all_results.items():
        file_size = info['file_size']
        extensions = info['extensions']

        lines.append(f"---")
        lines.append(f"\n## {field}")
        lines.append(f"\n**File size:** {file_size:,} bytes ({file_size/1e9:.3f} GB)")
        lines.append(f"**URL:** `{info['url']}`")
        lines.append(f"**Total extensions:** {len(extensions)}")
        lines.append("")

        lines.append("### Extension Summary")
        lines.append("")
        lines.append(f"| {'Ext':>3} | {'Name':<20} | {'Rows':>10} | {'Cols':>5} | {'Data Size':>12} |")
        lines.append(f"|{'---':>5}|{'-'*22}|{'-'*12}|{'-'*7}|{'-'*14}|")
        for ext in extensions:
            data_str = f"{ext['data_size']/1e6:.1f} MB"
            lines.append(f"| {ext['ext_num']:>3} | {ext['extname']:<20} | {ext['naxis2']:>10,} | {ext['tfields']:>5} | {data_str:>12} |")
        lines.append("")

        critical_exts = ['FLAG', 'PHOTOZ', 'PHOTOZ_KRON', 'SIZE', 'KRON', 'KRON_CONV', 'MIRI']
        for ext in extensions:
            if ext['extname'] in critical_exts and ext['columns']:
                lines.append(f"### {field} — {ext['extname']} ({ext['naxis2']:,} rows, {ext['tfields']} columns)")
                lines.append("")
                lines.append(format_column_table(ext['columns']))
                lines.append("")

        needed = check_research_columns(extensions)
        lines.append(f"### {field} — Research Column Availability")
        lines.append("")
        lines.append("| Needed For Research | Found? |")
        lines.append("|---------------------|--------|")
        for key, found in needed.items():
            status = "YES" if found else "NO"
            lines.append(f"| {key} | {status} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Summary & Conclusions")
    lines.append("")

    all_needed = {}
    for field, info in all_results.items():
        needed = check_research_columns(info['extensions'])
        for k, v in needed.items():
            if k not in all_needed:
                all_needed[k] = {}
            all_needed[k][field] = v

    all_found = all(all(field_vals.values()) for field_vals in all_needed.values())

    if all_found:
        lines.append("**All required columns are present in both fields.** The JADES DR5 photometric catalog contains:")
    else:
        lines.append("**Some columns may need further verification:**")

    lines.append("")
    for k, field_vals in all_needed.items():
        statuses = [f"{f}: {'YES' if v else 'NO'}" for f, v in field_vals.items()]
        lines.append(f"- {k}: {', '.join(statuses)}")

    lines.append("")
    lines.append("### Key Extensions for the Anomaly Search")
    lines.append("")
    lines.append("1. **FLAG** — Source ID, RA, Dec, per-band quality flags and weights")
    lines.append("2. **PHOTOZ** — EAZY photo-z from small-aperture photometry (z_peak, z_a, z_ml, z_spec, chi-squared comparisons at z<4/5/6/7)")
    lines.append("3. **PHOTOZ_KRON** — EAZY photo-z from Kron photometry (same columns as PHOTOZ)")
    lines.append("4. **SIZE** — Morphological parameters (R_kron, semi-major/minor axes, position angle)")
    lines.append("5. **KRON / KRON_CONV** — Kron aperture photometry in all NIRCam bands")
    lines.append("6. **MIRI** — MIRI photometry (F770W, F1000W, F1280W, etc.)")
    lines.append("7. **CIRC / CIRC_BSUB / CIRC_CONV / CIRC_BSUB_CONV** — Circular aperture photometry (multiple aperture sizes)")
    lines.append("")
    lines.append("### Recommended Query Strategy")
    lines.append("")
    lines.append("To build the z > 6 sample without downloading the full files:")
    lines.append("1. Download only the FLAG + PHOTOZ extensions (~230 MB for GOODS-N, ~360 MB for GOODS-S)")
    lines.append("2. Filter on z_peak > 6 or z_a > 6")
    lines.append("3. For surviving candidates, fetch KRON + SIZE data")
    lines.append("4. Only download CIRC/MIRI extensions if needed for specific analysis")
    lines.append("")

    return '\n'.join(lines)


def main():
    all_results = {}

    for field, url in CATALOGS.items():
        print(f"\n>>> Verifying file size for {field}...")
        file_size = get_file_size(url)
        print(f"    Exact size: {file_size:,} bytes ({file_size/1e9:.3f} GB)")

        extensions = scan_all_extensions(field, url, file_size)
        all_results[field] = {
            'url': url,
            'file_size': file_size,
            'extensions': extensions,
        }

    print("\n\n" + "="*70)
    print("  RESEARCH COLUMN CHECK")
    print("="*70)
    for field, info in all_results.items():
        needed = check_research_columns(info['extensions'])
        print(f"\n  {field}:")
        for k, v in needed.items():
            status = "FOUND" if v else "MISSING"
            print(f"    [{status:>7}] {k}")

    report = generate_report(all_results)
    out_path = "data/research/jades-dr5-schema.md"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        f.write(report)
    print(f"\n\nSchema report written to: {out_path}")
    print(f"Report size: {len(report):,} characters")

    json_path = "data/research/jades-dr5-schema.json"
    json_data = {}
    for field, info in all_results.items():
        json_data[field] = {
            'url': info['url'],
            'file_size': info['file_size'],
            'file_size_gb': round(info['file_size'] / 1e9, 3),
            'extensions': [{
                'ext_num': e['ext_num'],
                'extname': e['extname'],
                'naxis1': e['naxis1'],
                'naxis2': e['naxis2'],
                'tfields': e['tfields'],
                'data_size_bytes': e['data_size'],
                'data_size_mb': round(e['data_size'] / 1e6, 1),
                'columns': e['columns'],
            } for e in info['extensions']],
        }
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
    print(f"JSON schema written to: {json_path}")


if __name__ == '__main__':
    main()
