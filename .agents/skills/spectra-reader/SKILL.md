---
name: spectra-reader
description: Read and interpret astronomical spectra to extract basic information like redshift, emission/absorption lines, and object classification. Use when analyzing spectral data. WARNING - sensitive spectral interpretation should not rely on AI alone.
---

# Spectra Reader

## Purpose

Read spectra and extract basic information. Much of an object's identity is hidden in its spectrum.

## When to Use

- Analyzing spectral data from DESI, SDSS, JWST, or ALMA
- Determining redshift of an object
- Classifying object type (star, galaxy, quasar, etc.)
- Looking for emission or absorption features

## Key Spectral Features

### Emission Lines (object is emitting)
- **Lyman-alpha** (1216 A): Hydrogen, key for high-z galaxies
- **H-alpha** (6563 A): Star formation indicator
- **[OII]** (3727 A): Star formation at moderate z
- **[OIII]** (4959, 5007 A): AGN/starburst indicator
- **CIV** (1549 A): High-ionization, quasars

### Absorption Lines (intervening material)
- **Lyman break**: Hydrogen absorption cutoff, redshift indicator
- **CaII H&K** (3934, 3969 A): Old stellar populations
- **MgII** (2796, 2803 A): Intervening gas
- **Balmer series**: Stellar atmospheres

### Continuum Shape
- Blue continuum: Young stars, AGN
- Red continuum: Old stars, dust
- Flat: Mixed populations
- Power-law: AGN/quasar

## Process

1. **Load spectrum**: Wavelength vs flux
2. **Check quality**: S/N ratio, calibration status
3. **Identify redshift**: Find recognizable line patterns
4. **Mark features**: Emission lines, absorption lines, breaks
5. **Classify**: Star / galaxy / quasar / unknown
6. **Extract parameters**: Redshift, line fluxes, equivalent widths

## Output Format

```
## قراءة الطيف

### الملف: [filename]
- المصدر: [survey]
- الهدف: [object ID]
- المدى الطيفي: [wavelength range]
- نسبة الإشارة للضوضاء: [S/N]

### الانزياح الأحمر
- z = [value] ± [error]
- الثقة: [عالية / متوسطة / منخفضة]
- مبني على: [أي خطوط]

### الخطوط المكتشفة
| الخط | الموجة المرصودة | الموجة الأصلية | الشدة |
|------|----------------|----------------|-------|

### التصنيف
- النوع: [star/galaxy/quasar/unknown]
- التصنيف الفرعي: [if applicable]

### ملاحظات
[أي ملاحظات أو تحذيرات]
```

## AI Trust Warning

This skill is very useful, but **sensitive spectral interpretation should NOT rely on AI alone**:
- Redshift determination at z > 8 needs expert review
- Faint emission line detection needs human verification
- Unusual spectra that don't match templates need careful analysis
- Any spectrum leading to a "discovery" claim must be independently verified

AI is good at: pattern matching known features, quick classification, bulk processing
AI should NOT be trusted alone for: novel spectral features, very faint lines, controversial redshifts
