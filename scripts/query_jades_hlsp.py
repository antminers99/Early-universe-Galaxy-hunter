#!/usr/bin/env python3
"""
Try multiple approaches to get JADES DR5 catalog data without
downloading the full 6GB FITS files.
"""
import os
import sys

OUT_DIR = "data/catalogs/jades-dr5"
os.makedirs(OUT_DIR, exist_ok=True)

print("=== Approach 1: MAST HLSP-specific TAP ===")
try:
    import pyvo
    hlsp_tap = pyvo.dal.TAPService("https://mast.stsci.edu/vo-tap/api/v0.1/hlsp")
    tables = hlsp_tap.tables
    jades_tables = [t for t in tables.keys() if 'jades' in t.lower()]
    print(f"Found {len(jades_tables)} JADES tables:")
    for t in jades_tables[:20]:
        print(f"  {t}")
    if not jades_tables:
        print("No JADES tables found, listing all:")
        for t in list(tables.keys())[:30]:
            print(f"  {t}")
except Exception as e:
    print(f"HLSP TAP failed: {e}")

print("\n=== Approach 2: Try astropy remote FITS header read ===")
try:
    from astropy.io import fits
    url = "https://slate.ucsc.edu/~brant/jades-dr5/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits"
    print(f"Trying to open remote FITS: {url}")
    with fits.open(url, lazy_load_hdus=True, memmap=True) as hdulist:
        print(f"HDU list: {len(hdulist)} extensions")
        for i, hdu in enumerate(hdulist):
            print(f"  HDU {i}: {hdu.name} ({type(hdu).__name__})")
            if hasattr(hdu, 'columns') and hdu.columns is not None:
                print(f"    Columns: {len(hdu.columns)}")
                for col in hdu.columns[:10]:
                    print(f"      {col.name}: {col.format}")
                if len(hdu.columns) > 10:
                    print(f"      ... and {len(hdu.columns)-10} more")
                print(f"    Rows: {hdu.header.get('NAXIS2', '?')}")
except Exception as e:
    print(f"Remote FITS read failed: {e}")

print("\n=== Approach 3: Try MAST catalog portal ===")
try:
    from astroquery.mast import Catalogs
    print("Querying MAST Catalogs for JADES...")
    result = Catalogs.query_criteria(catalog="HLSP", hlsp_id="jades")
    print(f"Got {len(result)} results")
    if len(result) > 0:
        print(f"Columns: {result.colnames[:10]}")
except Exception as e:
    print(f"MAST Catalogs query failed: {e}")
