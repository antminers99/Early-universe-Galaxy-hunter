#!/usr/bin/env python3
import os
import urllib.request
import sys

BASE_URL = "https://slate.ucsc.edu/~brant/jades-dr5"
OUT_DIR = "data/catalogs/jades-dr5"

CATALOGS = [
    {
        "field": "GOODS-S",
        "url": f"{BASE_URL}/GOODS-S/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-s_photometry_v5.0_catalog.fits",
        "filename": "jades_dr5_goods-s_photometry.fits",
    },
    {
        "field": "GOODS-N",
        "url": f"{BASE_URL}/GOODS-N/hlsp/catalogs/hlsp_jades_jwst_nircam_goods-n_photometry_v5.0_catalog.fits",
        "filename": "jades_dr5_goods-n_photometry.fits",
    },
]

os.makedirs(OUT_DIR, exist_ok=True)

for cat in CATALOGS:
    dest = os.path.join(OUT_DIR, cat["filename"])
    if os.path.exists(dest):
        size_mb = os.path.getsize(dest) / 1e6
        print(f"[SKIP] {cat['field']} already exists ({size_mb:.1f} MB)")
        continue
    print(f"[DOWNLOAD] {cat['field']}: {cat['url']}")
    try:
        urllib.request.urlretrieve(cat["url"], dest)
        size_mb = os.path.getsize(dest) / 1e6
        print(f"[OK] {cat['field']}: {size_mb:.1f} MB")
    except Exception as e:
        print(f"[ERROR] {cat['field']}: {e}", file=sys.stderr)
        sys.exit(1)

print("\nAll catalogs downloaded successfully.")
