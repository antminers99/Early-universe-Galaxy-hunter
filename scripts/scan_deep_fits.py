#!/usr/bin/env python3
"""
Scan deeper into the JADES FITS files to find ALL extensions,
especially the EAZY photometric redshift tables.
"""
import urllib.request
import json

BASE_URL = "https://slate.ucsc.edu/~brant/jades-dr5"

FIELDS = {
    "GOODS-N": {
        "url": f"{BASE_URL}/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
        "total_size": 3116517120,
    },
}

BLOCK = 2880

def fetch_range(url, start, end):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()

def parse_header_at(url, offset):
    header_blocks = []
    pos = offset
    while True:
        data = fetch_range(url, pos, pos + BLOCK * 20 - 1)
        for b in range(0, len(data), BLOCK):
            chunk = data[b:b+BLOCK]
            try:
                text = chunk.decode('ascii', errors='replace')
            except:
                return None, 0
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
                    'naxis2': naxis2,
                    'tfields': int(cards.get('TFIELDS', 0)),
                    'columns': ttypes,
                    'offset': offset,
                    'data_offset': offset + header_size,
                    'data_size': data_size,
                    'total_size': total,
                    'naxis1': naxis1,
                }, total
        pos += BLOCK * 20
        if pos - offset > 1_000_000:
            return None, 0

for field, info in FIELDS.items():
    url = info['url']
    total_file_size = info['total_size']
    print(f"\n{'='*60}")
    print(f"Scanning ALL extensions in {field} ({total_file_size/1e9:.1f} GB)")
    print(f"{'='*60}")
    
    offset = 0
    ext_num = 0
    all_exts = []
    
    while offset < total_file_size:
        ext, size = parse_header_at(url, offset)
        if ext is None:
            print(f"  [STOP] Could not parse header at offset {offset}")
            break
        
        print(f"  Ext {ext_num}: {ext['extname'] or 'PRIMARY':20s} | rows={ext['naxis2']:>8} cols={ext['tfields']:>4} | size={ext['data_size']/1e6:>8.1f}MB | offset={offset}")
        
        relevant = [c for c in ext['columns'] if any(k in c.upper() for k in ['Z_', 'EAZY', 'MASS', 'MUV', 'BETA', 'SFR', 'REFF', 'AGE', 'AV_', 'SPEC', 'KRON'])]
        if relevant:
            print(f"           >>> RELEVANT: {relevant[:15]}")
        
        ext['index'] = ext_num
        all_exts.append(ext)
        offset += size
        ext_num += 1
    
    out_file = f"data/catalogs/jades-dr5/jades_dr5_{field.lower()}_full_structure.json"
    with open(out_file, 'w') as f:
        json.dump(all_exts, f, indent=2)
    print(f"\nFull structure saved to {out_file}")
