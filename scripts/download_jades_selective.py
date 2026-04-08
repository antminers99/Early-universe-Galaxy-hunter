#!/usr/bin/env python3
"""
Download only FLAG (ID/RA/DEC) + PHOTOZ + SIZE extensions from JADES DR5
using HTTP range requests. This avoids downloading the full 6GB+ files.
"""
import urllib.request
import os
import sys
import struct

BLOCK = 2880
OUT_DIR = "data/catalogs/jades-dr5"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()

def parse_header_at(url, offset):
    header_blocks = []
    pos = offset
    while True:
        data = fetch_range(url, pos, pos + BLOCK * 20 - 1)
        for b in range(0, len(data), BLOCK):
            chunk = data[b:b+BLOCK]
            text = chunk.decode('ascii', errors='replace')
            header_blocks.append(text)
            lines = [text[j:j+80] for j in range(0, BLOCK, 80)]
            if any(l[:3] == 'END' for l in lines):
                cards = {}
                for blk in header_blocks:
                    for j in range(0, BLOCK, 80):
                        line = blk[j:j+80]
                        key = line[:8].strip()
                        if key == 'END':
                            break
                        if '=' in line[:10]:
                            val = line[10:].split('/')[0].strip().strip("'").strip()
                            cards[key] = val

                header_size = len(header_blocks) * BLOCK
                naxis1 = int(cards.get('NAXIS1', 0))
                naxis2 = int(cards.get('NAXIS2', 0))
                pcount = int(cards.get('PCOUNT', 0))
                naxis = int(cards.get('NAXIS', 0))
                tfields = int(cards.get('TFIELDS', 0))

                if naxis >= 2:
                    data_size = naxis1 * naxis2 + pcount
                else:
                    data_size = 0

                data_blocks = (data_size + BLOCK - 1) // BLOCK
                total = header_size + data_blocks * BLOCK

                ttypes = []
                for k in sorted(cards.keys()):
                    if k.startswith('TTYPE'):
                        ttypes.append(cards[k])

                return {
                    'extname': cards.get('EXTNAME', ''),
                    'naxis1': naxis1,
                    'naxis2': naxis2,
                    'tfields': tfields,
                    'columns': ttypes,
                    'offset': offset,
                    'header_size': header_size,
                    'data_offset': offset + header_size,
                    'data_size': data_size,
                    'total_size': total,
                    'header_bytes': b''.join(blk.encode('ascii', errors='replace') for blk in header_blocks),
                }, total
        pos += BLOCK * 20
        if pos - offset > 2_000_000:
            return None, 0

def download_extensions(field, url, total_size, wanted_extnames):
    """Scan through the FITS file and download only the wanted extensions."""
    print(f"\n{'='*60}")
    print(f"Downloading selected extensions from {field}")
    print(f"File size: {total_size/1e9:.1f} GB")
    print(f"Wanted extensions: {wanted_extnames}")
    print(f"{'='*60}")

    offset = 0
    ext_num = 0
    collected = {}

    while offset < total_size:
        ext, size = parse_header_at(url, offset)
        if ext is None:
            print(f"  Could not parse at offset {offset}, stopping")
            break

        extname = ext['extname'] or 'PRIMARY'
        print(f"  Ext {ext_num}: {extname:20s} | rows={ext['naxis2']:>8} | size={ext['data_size']/1e6:>7.1f}MB", end="")

        if extname in wanted_extnames:
            print(f" [DOWNLOADING]")
            data_start = ext['data_offset']
            data_end = data_start + ext['data_size'] - 1

            chunk_size = 10 * 1024 * 1024
            all_data = bytearray()
            pos = data_start
            while pos <= data_end:
                end = min(pos + chunk_size - 1, data_end)
                chunk = fetch_range(url, pos, end)
                all_data.extend(chunk)
                pct = len(all_data) / ext['data_size'] * 100
                print(f"    {pct:.0f}% ({len(all_data)/1e6:.1f}/{ext['data_size']/1e6:.1f} MB)")
                pos = end + 1

            collected[extname] = {
                'header': ext['header_bytes'],
                'data': bytes(all_data),
                'ext': ext,
            }
        else:
            print(f" [SKIP]")

        offset += size
        ext_num += 1

        if len(collected) == len(wanted_extnames):
            print(f"\n  All wanted extensions collected!")
            break

    return collected


def write_mini_fits(field, collected):
    """Write a minimal FITS file with only the collected extensions."""
    from astropy.io import fits

    primary_header = fits.Header()
    primary_header['SIMPLE'] = True
    primary_header['BITPIX'] = 8
    primary_header['NAXIS'] = 0
    primary_header['EXTEND'] = True
    primary_header['HLSPID'] = 'JADES'
    primary_header['FIELD'] = field
    primary_header['HLSPVER'] = '5.0'
    primary_header['COMMENT'] = 'Subset of JADES DR5 catalog: FLAG + SIZE + PHOTOZ extensions only'

    hdu_list = [fits.PrimaryHDU(header=primary_header)]

    for extname in ['FLAG', 'SIZE', 'PHOTOZ', 'PHOTOZ_KRON']:
        if extname not in collected:
            continue
        info = collected[extname]
        header_bytes = info['header']
        data_bytes = info['data']
        ext = info['ext']

        naxis1 = ext['naxis1']
        naxis2 = ext['naxis2']
        total_expected = naxis1 * naxis2
        actual = len(data_bytes)
        if actual < total_expected:
            data_bytes = data_bytes + b'\x00' * (total_expected - actual)

        import numpy as np
        raw = np.frombuffer(data_bytes[:total_expected], dtype=np.uint8).reshape(naxis2, naxis1)

        header = fits.Header()
        header_text = header_bytes.decode('ascii', errors='replace')
        for j in range(0, len(header_text), 80):
            card = header_text[j:j+80]
            key = card[:8].strip()
            if key in ('', 'END', 'XTENSION', 'BITPIX', 'NAXIS', 'NAXIS1', 'NAXIS2', 'PCOUNT', 'GCOUNT', 'TFIELDS'):
                continue
            if '=' in card[:10]:
                try:
                    header.append(fits.Card.fromstring(card))
                except:
                    pass

        binhdu = fits.BinTableHDU.from_columns(
            fits.ColDefs.from_columns(
                fits.BinTableHDU(data=raw, header=None).columns
            ),
            header=header,
            nrows=naxis2,
        )
        binhdu.name = extname
        hdu_list.append(binhdu)
        print(f"  Added {extname}: {naxis2} rows, {ext['tfields']} cols")

    return fits.HDUList(hdu_list)


FIELDS = [
    {
        "name": "GOODS-N",
        "url": "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
        "total_size": 3116517120,
    },
]

WANTED = {'FLAG', 'SIZE', 'PHOTOZ', 'PHOTOZ_KRON'}

for field_info in FIELDS:
    field = field_info['name']
    url = field_info['url']
    total_size = field_info['total_size']

    collected = download_extensions(field, url, total_size, WANTED)

    if 'PHOTOZ' not in collected:
        print(f"\n  ERROR: PHOTOZ extension not found for {field}")
        sys.exit(1)

    from astropy.io import fits
    from astropy.table import Table
    import pandas as pd
    import numpy as np

    photoz_ext = collected['PHOTOZ']
    photoz_header = photoz_ext['header']
    photoz_data = photoz_ext['data']
    photoz_info = photoz_ext['ext']

    flag_ext = collected['FLAG']
    flag_data = flag_ext['data']
    flag_info = flag_ext['ext']

    print(f"\nParsing PHOTOZ table with astropy...")
    print(f"  PHOTOZ: {photoz_info['naxis2']} rows x {photoz_info['naxis1']} bytes/row")

    photoz_bytes = photoz_ext['header'] + photoz_data
    pad_needed = BLOCK - (len(photoz_bytes) % BLOCK) if len(photoz_bytes) % BLOCK != 0 else 0
    photoz_bytes += b'\x00' * pad_needed

    flag_bytes = flag_ext['header'] + flag_data
    pad_needed2 = BLOCK - (len(flag_bytes) % BLOCK) if len(flag_bytes) % BLOCK != 0 else 0
    flag_bytes += b'\x00' * pad_needed2

    primary = fits.PrimaryHDU()
    primary_bytes = primary.header.tostring().encode('ascii')
    pad_primary = BLOCK - (len(primary_bytes) % BLOCK) if len(primary_bytes) % BLOCK != 0 else 0
    primary_bytes += b' ' * pad_primary

    mini_fits = primary_bytes + flag_bytes + photoz_bytes
    out_path = os.path.join(OUT_DIR, f"jades_dr5_{field.lower()}_subset.fits")
    with open(out_path, 'wb') as f:
        f.write(mini_fits)
    print(f"  Written to {out_path} ({len(mini_fits)/1e6:.1f} MB)")

    try:
        with fits.open(out_path) as hdulist:
            print(f"\n  Verifying FITS file:")
            for i, hdu in enumerate(hdulist):
                print(f"    HDU {i}: {hdu.name} ({type(hdu).__name__})")
                if hasattr(hdu, 'columns') and hdu.columns:
                    print(f"      Columns: {len(hdu.columns)}")
                    print(f"      Rows: {hdu.data.shape[0] if hdu.data is not None else 0}")
    except Exception as e:
        print(f"  Verification failed: {e}")
        print(f"  Will try to parse tables directly instead...")

print("\nDone!")
