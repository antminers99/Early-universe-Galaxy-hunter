---
name: source-finder
description: Find and catalog important astronomical data sources from the web. Use when the user asks to find data sources, discover new archives, or locate datasets for a research question about the early universe.
---

# Source Finder

## Purpose

Find all important data sources from the web relevant to a research question or topic in early universe cosmology.

## When to Use

- User asks to find data sources for a specific topic
- Starting a new research question and need to identify available data
- Expanding the catalog with new sources
- Checking if new data releases are available

## Process

1. **Understand the topic**: What specific aspect of the early universe are we investigating?
2. **Search known archives first**:
   - MAST (JWST, Hubble, Kepler)
   - ESA archives (Planck, Euclid)
   - NASA LAMBDA (CMB experiments)
   - ALMA Science Archive
   - SDSS, DESI
   - HERA, MWA (reionization)
   - GWOSC (gravitational waves)
3. **Search for new/lesser-known sources**:
   - Use web search to find recent data releases
   - Check arXiv for papers announcing new public datasets
   - Look at survey telescope data release pages
4. **For each source found, record**:
   - Name and URL
   - Approximate size
   - Data format (FITS, HDF5, CSV, etc.)
   - Coverage (sky area, redshift range, wavelength)
   - Access method (web download, API, bulk download)
   - Priority level (essential / important / supplementary)
   - Relevance to the research question

## Output Format

```
## مصادر البيانات - [الموضوع]

### مصادر أساسية
| المصدر | الحجم | الصيغة | الوصول | الرابط |
|--------|-------|--------|--------|--------|

### مصادر مهمة
[same table format]

### مصادر تكميلية
[same table format]

### ملخص
- عدد المصادر: X
- الحجم الإجمالي التقريبي: X
- أهم مصدر للبدء: [name]
```

## Key Data Archives Reference

- **MAST**: mast.stsci.edu — JWST, Hubble, TESS
- **Planck Legacy Archive**: pla.esac.esa.int — CMB maps
- **NASA LAMBDA**: lambda.gsfc.nasa.gov — CMB data & tools
- **ALMA**: almascience.nrao.edu — sub-mm/radio
- **Euclid**: cosmos.esa.int/web/euclid — dark energy survey
- **DESI**: data.desi.lbl.gov — spectroscopic survey
- **SDSS**: sdss.org — optical spectroscopic survey
- **HERA**: reionization.org — 21-cm reionization
- **GWOSC**: gwosc.org — gravitational waves
- **NED**: ned.ipac.caltech.edu — extragalactic database
- **VizieR**: vizier.cds.unistra.fr — catalog service

## AI Notes

- Always verify URLs are current and accessible
- Check for data access restrictions or embargo periods
- Note if registration is required for data access
- Flag any sources that require specific software to read
