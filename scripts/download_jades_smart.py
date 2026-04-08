#!/usr/bin/env python3
"""
Smart JADES DR5 catalog access:
Strategy: Use fsspec + astropy to stream-read only the needed columns
from the remote FITS files without downloading the full 6GB files.
Falls back to downloading extension-by-extension if streaming fails.
"""
import os
import sys
import struct
import urllib.request
import io
import json

BASE_URL = "https://slate.ucsc.edu/~brant/jades-dr5"
OUT_DIR = "data/catalogs/jades-dr5"
os.makedirs(OUT_DIR, exist_ok=True)

FIELDS = {
    "GOODS-S": f"{BASE_URL}/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
    "GOODS-N": f"{BASE_URL}/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
}

def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()

def parse_fits_headers(url, max_bytes=10_000_000):
    """Parse all FITS extension headers using range requests."""
    block = 2880
    offset = 0
    extensions = []

    while offset < max_bytes:
        data = fetch_range(url, offset, offset + block * 40 - 1)
        header_str = ""
        header_cards = {}
        blocks_read = 0

        for b in range(0, len(data), block):
            chunk = data[b:b+block]
            try:
                text = chunk.decode('ascii', errors='replace')
            except:
                break
            blocks_read += 1

            lines = [text[j:j+80] for j in range(0, block, 80)]
            for line in lines:
                key = line[:8].strip()
                if key == 'END':
                    break
                if '=' in line[:10]:
                    val = line[10:].split('/')[0].strip().strip("'").strip()
                    header_cards[key] = val
            if any(l[:3] == 'END' for l in lines):
                break

        header_size = blocks_read * block
        ext_info = {
            'offset': offset,
            'header_size': header_size,
            'cards': header_cards,
        }

        xtension = header_cards.get('XTENSION', '')
        extname = header_cards.get('EXTNAME', '')
        naxis1 = int(header_cards.get('NAXIS1', 0))
        naxis2 = int(header_cards.get('NAXIS2', 0))
        bitpix = int(header_cards.get('BITPIX', 0))
        naxis = int(header_cards.get('NAXIS', 0))
        tfields = int(header_cards.get('TFIELDS', 0))
        pcount = int(header_cards.get('PCOUNT', 0))

        if naxis == 0:
            data_size = 0
        elif naxis >= 2:
            data_size = naxis1 * naxis2 + pcount
        else:
            data_size = abs(bitpix) // 8 * int(header_cards.get('NAXIS1', 0))

        data_blocks = (data_size + block - 1) // block
        total_size = header_size + data_blocks * block

        ext_info['data_offset'] = offset + header_size
        ext_info['data_size'] = data_size
        ext_info['total_size'] = total_size
        ext_info['extname'] = extname
        ext_info['naxis2'] = naxis2
        ext_info['tfields'] = tfields

        ttypes = []
        for k, v in sorted(header_cards.items()):
            if k.startswith('TTYPE'):
                ttypes.append(v)
        ext_info['columns'] = ttypes

        extensions.append(ext_info)
        print(f"  Extension {len(extensions)-1}: {extname or 'PRIMARY'} | rows={naxis2} cols={tfields} | data={data_size/1e6:.1f}MB")

        offset += total_size
        if offset >= max_bytes and naxis2 == 0:
            continue
        if len(extensions) > 1 and naxis2 == 0 and len(ttypes) == 0:
            break

    return extensions

for field, url in FIELDS.items():
    print(f"\n{'='*60}")
    print(f"Parsing {field} catalog structure...")
    print(f"{'='*60}")
    exts = parse_fits_headers(url, max_bytes=200_000_000)

    out_file = os.path.join(OUT_DIR, f"jades_dr5_{field.lower()}_structure.json")
    with open(out_file, 'w') as f:
        json.dump([{
            'index': i,
            'extname': e['extname'],
            'naxis2': e['naxis2'],
            'tfields': e['tfields'],
            'columns': e['columns'],
            'data_offset': e['data_offset'],
            'data_size': e['data_size'],
        } for i, e in enumerate(exts)], f, indent=2)
    print(f"Structure saved to {out_file}")
