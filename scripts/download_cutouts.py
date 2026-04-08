#!/usr/bin/env python3
"""
Download small JWST JADES DR5 cutouts for the 35 triple-overlap candidates.
Uses HTTP range requests on the remote FITS mosaics (no full download needed).
Saves as PNG images with proper astronomical stretch.
"""
import csv
import math
import os
import struct
import urllib.request
import numpy as np
from datetime import datetime, timezone

WCS_PARAMS = {
    'GOODS-S': {
        'base_url': 'https://slate.ucsc.edu/~brant/jades-dr5/GOODS-S/hlsp/images/mosaics',
        'crpix1': 22972.5, 'crpix2': 27629.5,
        'crval1': 53.122781107619, 'crval2': -27.805160455556,
        'cdelt1': 8.33187749999999e-06, 'cdelt2': 8.33187749999999e-06,
        'pc1_1': -1.0, 'pc1_2': 0.0, 'pc2_1': 0.0, 'pc2_2': 1.0,
        'naxis1': 46700, 'naxis2': 46000,
    },
}

FILTERS = ['f150w', 'f200w', 'f277w', 'f356w', 'f444w']
CUTOUT_HALF = 30
PRIMARY_HDU_SIZE = 2880 * 10


def to_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def radec_to_pixel(ra, dec, wcs):
    ra0 = wcs['crval1']
    dec0 = wcs['crval2']
    dec_rad = math.radians(dec)
    dec0_rad = math.radians(dec0)

    xi = math.cos(dec_rad) * math.sin(math.radians(ra - ra0))
    xi /= (math.cos(dec0_rad) * math.cos(dec_rad) * math.cos(math.radians(ra - ra0)) +
           math.sin(dec0_rad) * math.sin(dec_rad))
    eta = (math.cos(dec0_rad) * math.sin(dec_rad) -
           math.sin(dec0_rad) * math.cos(dec_rad) * math.cos(math.radians(ra - ra0)))
    eta /= (math.cos(dec0_rad) * math.cos(dec_rad) * math.cos(math.radians(ra - ra0)) +
            math.sin(dec0_rad) * math.sin(dec_rad))

    xi_deg = math.degrees(xi)
    eta_deg = math.degrees(eta)

    pc11 = wcs.get('pc1_1', -1.0)
    pc12 = wcs.get('pc1_2', 0.0)
    pc21 = wcs.get('pc2_1', 0.0)
    pc22 = wcs.get('pc2_2', 1.0)

    cd11 = pc11 * wcs['cdelt1']
    cd12 = pc12 * wcs['cdelt2']
    cd21 = pc21 * wcs['cdelt1']
    cd22 = pc22 * wcs['cdelt2']

    det = cd11 * cd22 - cd12 * cd21
    inv11 = cd22 / det
    inv12 = -cd12 / det
    inv21 = -cd21 / det
    inv22 = cd11 / det

    dx = inv11 * xi_deg + inv12 * eta_deg
    dy = inv21 * xi_deg + inv22 * eta_deg

    x = wcs['crpix1'] + dx
    y = wcs['crpix2'] + dy

    return int(round(x)), int(round(y))


def get_fits_header_size(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    req.add_header('Range', 'bytes=0-57600')
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    
    pos = 0
    total_hdr = 0
    ext_count = 0
    
    while pos < len(data):
        block = data[pos:pos+2880]
        if len(block) < 2880:
            break
        
        hdr_end = False
        for i in range(0, 2880, 80):
            card = block[i:i+80].decode('ascii', errors='replace')
            if card[:8].strip() == 'END':
                hdr_end = True
                break
        
        if hdr_end:
            pos += 2880
            ext_count += 1
            
            if ext_count == 1:
                total_hdr = pos
                continue
            else:
                break
        pos += 2880
    
    naxis1 = naxis2 = 0
    bitpix = -32
    
    text = data[total_hdr:pos].decode('ascii', errors='replace')
    for i in range(0, len(text), 80):
        card = text[i:i+80]
        key = card[:8].strip()
        if key == 'NAXIS1':
            naxis1 = int(card.split('=')[1].split('/')[0].strip())
        elif key == 'NAXIS2':
            naxis2 = int(card.split('=')[1].split('/')[0].strip())
        elif key == 'BITPIX':
            bitpix = int(card.split('=')[1].split('/')[0].strip())
    
    return total_hdr + (pos - total_hdr), naxis1, naxis2, bitpix


def download_cutout_pixels(url, px, py, half, hdr_offset, naxis1, naxis2, bitpix=-32):
    bpp = abs(bitpix) // 8
    
    x0 = max(0, px - half)
    x1 = min(naxis1, px + half)
    y0 = max(0, py - half)
    y1 = min(naxis2, py + half)
    
    if x0 >= x1 or y0 >= y1:
        return None
    
    width = x1 - x0
    height = y1 - y0
    
    row_bytes = naxis1 * bpp
    
    rows_data = np.full((height, width), np.nan, dtype=np.float32)
    
    start_row = y0
    end_row = y1
    
    byte_start = hdr_offset + start_row * row_bytes + x0 * bpp
    byte_end = hdr_offset + (end_row - 1) * row_bytes + x1 * bpp - 1
    
    total_bytes = byte_end - byte_start + 1
    
    if total_bytes > 50_000_000:
        chunk_size = 5
        for chunk_start in range(start_row, end_row, chunk_size):
            chunk_end = min(chunk_start + chunk_size, end_row)
            b_start = hdr_offset + chunk_start * row_bytes + x0 * bpp
            b_end = hdr_offset + (chunk_end - 1) * row_bytes + x1 * bpp - 1
            
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            req.add_header('Range', f'bytes={b_start}-{b_end}')
            
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
            
            for row_i in range(chunk_end - chunk_start):
                row_offset = row_i * row_bytes
                row_data = raw[row_offset:row_offset + width * bpp]
                if len(row_data) == width * bpp:
                    rows_data[chunk_start - start_row + row_i] = np.frombuffer(row_data, dtype='>f4')
    else:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Range', f'bytes={byte_start}-{byte_end}')
        
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
        
        for row_i in range(height):
            row_offset = row_i * row_bytes
            row_data = raw[row_offset:row_offset + width * bpp]
            if len(row_data) == width * bpp:
                rows_data[row_i] = np.frombuffer(row_data, dtype='>f4')
    
    return rows_data


def asinh_stretch(data, scale=0.02):
    valid = data[~np.isnan(data)]
    if len(valid) == 0:
        return np.zeros_like(data, dtype=np.uint8)
    
    data_range = np.max(valid) - np.min(valid)
    if data_range < 1e-12:
        return np.zeros_like(data, dtype=np.uint8)
    
    median_val = np.median(valid)
    mad = np.median(np.abs(valid - median_val))
    sigma = mad * 1.4826
    
    if sigma <= 1e-12:
        sigma = np.std(valid)
    if sigma <= 1e-12:
        return np.zeros_like(data, dtype=np.uint8)
    
    vmin = median_val - 1.0 * sigma
    vmax = median_val + 8.0 * sigma
    
    normalized = (data - vmin) / (vmax - vmin)
    normalized = np.clip(normalized, 0, 1)
    
    stretched = np.arcsinh(normalized / scale) / np.arcsinh(1.0 / scale)
    stretched = np.clip(stretched, 0, 1)
    
    result = (stretched * 255).astype(np.uint8)
    result[np.isnan(data)] = 0
    
    return result


def save_png(pixels, filepath):
    import zlib
    
    height, width = pixels.shape
    
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'
        for x in range(width):
            v = pixels[y, x]
            raw_data += bytes([v, v, v])
    
    def make_chunk(chunk_type, data):
        chunk = chunk_type + data
        crc = zlib.crc32(chunk) & 0xffffffff
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', crc)
    
    png = b'\x89PNG\r\n\x1a\n'
    
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    png += make_chunk(b'IHDR', ihdr_data)
    
    compressed = zlib.compress(raw_data, 9)
    png += make_chunk(b'IDAT', compressed)
    
    png += make_chunk(b'IEND', b'')
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        f.write(png)


def main():
    print("=" * 70)
    print("  Download JWST JADES DR5 Cutouts for 35 Triple Candidates")
    print(f"  {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 70)
    
    features = {}
    with open('data/research/sample_b_features_v1.csv') as f:
        for r in csv.DictReader(f):
            features[(r['field'], r['ID'])] = r
    
    triples = []
    with open('data/research/overlap_candidates_v1.csv') as f:
        for r in csv.DictReader(f):
            if int(r['num_hunts']) == 3:
                feat = features.get((r['field'], r['ID']), {})
                triples.append({
                    'field': r['field'],
                    'id': r['ID'],
                    'ra': to_float(feat.get('RA')),
                    'dec': to_float(feat.get('DEC')),
                })
    
    print(f"\n  Candidates: {len(triples)}")
    
    gs_candidates = [t for t in triples if t['field'] == 'GOODS-S']
    gn_candidates = [t for t in triples if t['field'] == 'GOODS-N']
    print(f"    GOODS-S: {len(gs_candidates)}")
    print(f"    GOODS-N: {len(gn_candidates)}")
    
    print(f"\n  Getting GOODS-N WCS...")
    gn_base = 'https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/images/mosaics'
    gn_url = f'{gn_base}/hlsp_jades_jwst_nircam_goods-n_f444w_v5.0_drz.fits'
    req = urllib.request.Request(gn_url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    req.add_header('Range', 'bytes=0-57600')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            hdr_data = resp.read()
        
        text = hdr_data.decode('ascii', errors='replace')
        gn_wcs = {'base_url': gn_base}
        for i in range(0, len(text), 80):
            card = text[i:i+80]
            key = card[:8].strip()
            val_str = card[10:].split('/')[0].strip().strip("'").strip()
            if key == 'CRPIX1' and 'NAXIS' not in text[max(0,i-800):i]:
                pass
            if key in ('CRPIX1', 'CRPIX2', 'CRVAL1', 'CRVAL2', 'CDELT1', 'CDELT2',
                       'PC1_1', 'PC1_2', 'PC2_1', 'PC2_2'):
                try:
                    gn_wcs[key.lower()] = float(val_str)
                except:
                    pass
            elif key in ('NAXIS1', 'NAXIS2'):
                try:
                    v = int(val_str)
                    if v > 1000:
                        gn_wcs[key.lower()] = v
                except:
                    pass
        
        print(f"    GOODS-N WCS: CRVAL=({gn_wcs.get('crval1',0):.4f}, {gn_wcs.get('crval2',0):.4f})")
        print(f"    GOODS-N size: {gn_wcs.get('naxis1',0)}x{gn_wcs.get('naxis2',0)}")
        WCS_PARAMS['GOODS-N'] = gn_wcs
    except Exception as e:
        print(f"    ERROR getting GOODS-N WCS: {e}")
        if gn_candidates:
            print(f"    WARNING: Will skip {len(gn_candidates)} GOODS-N candidates")
    
    outdir = 'artifacts/data-app/public/cutouts'
    os.makedirs(outdir, exist_ok=True)
    
    hdr_cache = {}
    
    total = 0
    errors = 0
    
    for field_name, field_candidates in [('GOODS-S', gs_candidates), ('GOODS-N', gn_candidates)]:
        if field_name not in WCS_PARAMS:
            print(f"\n  Skipping {field_name} (no WCS)")
            continue
        
        wcs = WCS_PARAMS[field_name]
        field_tag = 'goods-s' if field_name == 'GOODS-S' else 'goods-n'
        
        print(f"\n  Processing {field_name} ({len(field_candidates)} candidates)...")
        
        for filt in FILTERS:
            url = f"{wcs['base_url']}/hlsp_jades_jwst_nircam_{field_tag}_{filt}_v5.0_drz.fits"
            
            cache_key = f"{field_name}_{filt}"
            if cache_key not in hdr_cache:
                print(f"\n    Reading {filt.upper()} header...")
                try:
                    hdr_size, nx, ny, bp = get_fits_header_size(url)
                    hdr_cache[cache_key] = (hdr_size, nx, ny, bp)
                    print(f"      Header: {hdr_size} bytes, image: {nx}x{ny}, bitpix: {bp}")
                except Exception as e:
                    print(f"      ERROR: {e}")
                    hdr_cache[cache_key] = None
                    continue
            
            cached = hdr_cache[cache_key]
            if cached is None:
                continue
            
            hdr_size, nx, ny, bp = cached
            
            for cand in field_candidates:
                cid = cand['id']
                ra = cand['ra']
                dec = cand['dec']
                
                if ra is None or dec is None:
                    continue
                
                px, py = radec_to_pixel(ra, dec, wcs)
                
                if px < 0 or px >= nx or py < 0 or py >= ny:
                    print(f"      {field_name} ID={cid}: pixel ({px},{py}) outside image")
                    errors += 1
                    continue
                
                png_path = f"{outdir}/{field_tag}_{cid}_{filt}.png"
                
                if os.path.exists(png_path) and os.path.getsize(png_path) > 100:
                    total += 1
                    continue
                
                try:
                    pixels = download_cutout_pixels(url, px, py, CUTOUT_HALF, hdr_size, nx, ny, bp)
                    
                    if pixels is not None:
                        stretched = asinh_stretch(pixels, scale=0.05)
                        
                        stretched = np.flipud(stretched)
                        
                        save_png(stretched, png_path)
                        total += 1
                        
                        if total % 10 == 0:
                            print(f"      Downloaded {total} cutouts...")
                    else:
                        errors += 1
                
                except Exception as e:
                    print(f"      ERROR {field_name} ID={cid} {filt}: {e}")
                    errors += 1
    
    print(f"\n  {'='*50}")
    print(f"  DONE: {total} cutouts saved, {errors} errors")
    print(f"  Output: {outdir}/")
    
    listing = os.listdir(outdir)
    if listing:
        print(f"  Files: {len(listing)}")
        sizes = [os.path.getsize(f"{outdir}/{f}") for f in listing]
        print(f"  Total size: {sum(sizes)/1024:.1f} KB")
        print(f"  Avg size: {sum(sizes)/len(sizes)/1024:.1f} KB")


if __name__ == '__main__':
    main()
