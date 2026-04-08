#!/usr/bin/env python3
"""
Query JADES DR5 photometric catalog from MAST via TAP service.
Downloads only the columns we need instead of the full 6GB FITS file.
"""
import os
import sys

try:
    from astroquery.mast import Mast
    from astropy.table import Table
    import pandas as pd
    import numpy as np
except ImportError as e:
    print(f"Missing package: {e}", file=sys.stderr)
    sys.exit(1)

OUT_DIR = "data/catalogs/jades-dr5"
os.makedirs(OUT_DIR, exist_ok=True)

print("Querying MAST for JADES DR5 catalog info...")

from astroquery.mast import Observations

results = Observations.query_criteria(
    project="HLSP",
    provenance_name="JADES",
    dataproduct_type="catalog",
)

print(f"Found {len(results)} HLSP entries")
if len(results) > 0:
    for row in results:
        print(f"  - {row['obs_id']} | {row['dataproduct_type']} | {row['target_name']}")
