#!/usr/bin/env python3
"""
Query JADES DR5 catalog via MAST TAP service using pyVO.
Only fetches the columns we need for z>6 galaxy analysis.
"""
import os
import sys
import pyvo

OUT_DIR = "data/catalogs/jades-dr5"
os.makedirs(OUT_DIR, exist_ok=True)

MAST_TAP_URL = "https://mast.stsci.edu/vo-tap/api/v0.1/caom"

print("Connecting to MAST TAP service...")
service = pyvo.dal.TAPService(MAST_TAP_URL)

print("Listing available tables...")
tables = service.tables
for tname in list(tables.keys())[:30]:
    print(f"  {tname}")
