---
name: download-manager
description: Download, organize, and store astronomical data files with clear naming conventions. Use when the user needs to download datasets, organize existing files, or set up a data directory structure.
---

# Download Manager

## Purpose

Download data files, organize them with clear naming, and track what we have so we don't get lost in files.

## When to Use

- Need to download data from an archive
- Organizing existing downloaded files
- Setting up directory structure for a new investigation
- Tracking what's been downloaded and what's pending

## Directory Structure

```
data/
├── raw/                    # Original downloaded files, never modified
│   ├── jwst/
│   │   ├── nircam/
│   │   └── miri/
│   ├── planck/
│   ├── desi/
│   ├── sdss/
│   ├── alma/
│   ├── euclid/
│   ├── hera/
│   └── gwosc/
├── processed/              # Cleaned and prepared data
│   └── [same structure]
├── catalogs/               # Cross-matched catalogs
├── metadata/               # File metadata and logs
│   └── download_log.json
└── README.md               # What's in this directory
```

## Naming Convention

```
{source}_{instrument}_{target}_{date}_{version}.{ext}

Examples:
jwst_nircam_smacs0723_2022-07-12_v1.fits
planck_hfi_353ghz_fullsky_2018_v3.fits
desi_spectra_dr1_bright_2024_v1.fits
```

## Download Log Format

Track every download in `metadata/download_log.json`:

```json
{
  "downloads": [
    {
      "id": "dl_001",
      "source": "MAST",
      "url": "https://...",
      "filename": "jwst_nircam_...",
      "size_mb": 1200,
      "date_downloaded": "2025-04-08",
      "checksum_sha256": "abc123...",
      "status": "complete",
      "notes": "SMACS 0723 deep field NIRCam F200W"
    }
  ]
}
```

## Process

1. **Identify what to download**: From Source Finder results
2. **Check if already downloaded**: Search download log
3. **Create target directory**: Following structure above
4. **Download with verification**:
   - Use checksums when available
   - Verify file size matches expected
   - Log the download
5. **Verify file integrity**: Can it be opened? Is the format correct?
6. **Update the log**

## Output Format

```
## تقرير التنزيل

### تم التنزيل
| الملف | المصدر | الحجم | الحالة |
|-------|--------|-------|--------|

### فشل التنزيل
[same format with error reason]

### ملخص
- عدد الملفات: X
- الحجم الإجمالي: X GB
- المسار: data/raw/[source]/
```

## AI Notes

- Never modify raw downloaded files — always work on copies
- Always verify checksums when available
- Large downloads (>10 GB) should note estimated time
- Flag files that require special software to read
