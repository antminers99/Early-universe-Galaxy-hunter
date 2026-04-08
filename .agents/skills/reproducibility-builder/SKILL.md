---
name: reproducibility-builder
description: Ensure every analysis step is reproducible from scratch. Use when building analysis pipelines, documenting workflows, or verifying that results can be regenerated. If we can't reproduce a result, we can't trust it.
---

# Reproducibility Builder

## Purpose

Make every step in our research reproducible from scratch. If we cannot reproduce a result, we cannot trust it.

## When to Use

- After completing any analysis step
- When documenting a workflow
- Before sharing results
- When verifying previous work

## Requirements for Reproducibility

### 1. Data Provenance
- Exact source URL and download date
- File checksums (SHA-256)
- Version of the dataset used
- Any selection criteria applied

### 2. Environment
- Software versions (Python, astropy, numpy, etc.)
- Package requirements file
- Operating system details if relevant
- Random seeds used in any stochastic process

### 3. Code
- All scripts used, version controlled
- No hardcoded paths — use configuration files
- Clear input/output specifications
- Comments explaining non-obvious choices

### 4. Parameters
- Every parameter used in analysis
- Why each parameter was chosen
- Sensitivity to parameter changes (link to Robustness Checker)

### 5. Steps Log
```json
{
  "pipeline": "early_galaxy_analysis",
  "steps": [
    {
      "step": 1,
      "name": "download_data",
      "input": "MAST query for JWST NIRCam z>10",
      "output": "data/raw/jwst/nircam_z10.fits",
      "script": "scripts/01_download.py",
      "timestamp": "2025-04-08T10:00:00Z",
      "checksum_output": "abc123..."
    }
  ]
}
```

## Output Format

```
## تقرير قابلية الإعادة

### المشروع: [name]

### خطوات التحليل
| الخطوة | المدخل | المخرج | السكريبت | قابل للإعادة؟ |
|--------|--------|--------|----------|--------------|

### البيئة
- Python: X.X
- الحزم: [list]

### البيانات
- المصدر: [source]
- التاريخ: [date]
- Checksum: [hash]

### الحالة
- [ ] كل الخطوات موثقة
- [ ] كل الأكواد محفوظة
- [ ] كل المعاملات مسجلة
- [ ] تم إعادة التشغيل بنجاح من الصفر
```

## AI Notes

- Test reproducibility by actually re-running from scratch when possible
- Version control is not optional — every script must be tracked
- Document failed attempts too — they're part of the research record
- Random seeds must be recorded for any ML or Monte Carlo work
