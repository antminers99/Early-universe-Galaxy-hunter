---
name: metadata-reader
description: Read and interpret metadata from astronomical data files. Use when the user needs to understand a file's origin, type, instrument, observation details, or data structure before analysis.
---

# Metadata Reader

## Purpose

Understand every file: where it came from, what type it is, what instrument was used, and what it contains. A file without its metadata cannot be properly understood.

## When to Use

- Received new data files and need to understand them
- Need to verify file contents before analysis
- Building a catalog of available data
- Checking if files are compatible for cross-matching

## Key Metadata Fields by Format

### FITS Files (most common in astronomy)
- **TELESCOP**: Telescope name
- **INSTRUME**: Instrument name
- **FILTER**: Filter/band used
- **DATE-OBS**: Observation date
- **EXPTIME**: Exposure time
- **RA/DEC**: Sky coordinates
- **OBJECT**: Target name
- **NAXIS1/2**: Image dimensions
- **BUNIT**: Data units
- **EQUINOX**: Coordinate epoch
- **WCSAXES**: WCS info for coordinates

### HDF5 Files (HERA, some simulations)
- Group hierarchy and dataset names
- Attributes on each group/dataset
- Data types and shapes
- Compression info

### VOTable (Euclid, VizieR)
- Table columns and types
- UCDs (Unified Content Descriptors)
- Units for each column

## Process

1. **Identify file format**: FITS, HDF5, CSV, VOTable, MS
2. **Extract header/metadata**: Using appropriate tools
3. **Parse key information**:
   - Source telescope/instrument
   - Observation parameters
   - Sky coverage
   - Data dimensions and types
   - Units and coordinate system
4. **Assess data quality indicators**:
   - Exposure time
   - Signal-to-noise markers
   - Calibration status
   - Known issues or flags

## Output Format

```
## معلومات الملف

### الملف: [filename]
- **المصدر**: [telescope/survey]
- **الأداة**: [instrument]
- **التاريخ**: [observation date]
- **الهدف**: [target/field]
- **الإحداثيات**: RA=XX, Dec=YY
- **الحجم**: [file size]
- **الأبعاد**: [dimensions]
- **الصيغة**: [format]
- **الوحدات**: [units]
- **جودة المعايرة**: [calibration status]

### ملاحظات
[أي تنبيهات أو مشاكل معروفة]
```

## AI Notes

- FITS headers can be very long — focus on key fields
- Some metadata may be in separate documentation, not in the file
- Flag files with missing critical metadata
- Note coordinate system differences between datasets (J2000 vs ICRS etc.)
