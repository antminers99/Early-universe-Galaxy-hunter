---
name: catalog-cross-matcher
description: Link the same astronomical object across multiple data sources by matching coordinates and properties. Use when combining data from different surveys or telescopes to build a complete picture of an object.
---

# Catalog Cross-Matcher

## Purpose

Link the same celestial object across multiple data sources so we see the complete picture, not just one piece.

## When to Use

- Combining data from JWST + Hubble + ALMA for the same field
- Matching DESI spectra to SDSS photometry
- Building multi-wavelength catalogs
- Verifying detections across independent surveys

## Process

1. **Identify catalogs to match**: Which surveys overlap?
2. **Choose matching method**:
   - **Positional**: Match by sky coordinates (RA, Dec) within a tolerance
   - **Property-based**: Match by brightness, redshift, or other properties
   - **Combined**: Position + property constraints
3. **Set matching radius**: Depends on instrument resolution
   - JWST NIRCam: ~0.1 arcsec
   - Hubble ACS: ~0.1 arcsec
   - ALMA: ~0.5-1.0 arcsec
   - SDSS: ~1.0 arcsec
   - Planck: ~5 arcmin (very different scale)
4. **Handle ambiguity**:
   - Multiple matches within radius → take nearest or flag
   - No match → record as unmatched
   - One-to-many → flag for review
5. **Validate matches**:
   - Check if matched properties are consistent
   - Compare photometry across bands
   - Flag suspicious matches

## Output Format

```
## تقرير التطابق بين الكتالوجات

### الكتالوجات
- الكتالوج 1: [name] — [N] أجرام
- الكتالوج 2: [name] — [N] أجرام

### المعاملات
- نصف قطر التطابق: [X] arcsec
- طريقة التطابق: [positional/combined]

### النتائج
| الحالة | العدد | النسبة |
|--------|-------|--------|
| تطابق فريد | XX | XX% |
| تطابق متعدد | XX | XX% |
| بدون تطابق (كتالوج 1) | XX | XX% |
| بدون تطابق (كتالوج 2) | XX | XX% |

### الأجرام المشبوهة
[أجرام التطابق فيها غير مؤكد]

### ملخص
[ملاحظات عامة عن جودة التطابق]
```

## AI Notes

- Different surveys have different coordinate precisions — account for this
- Some objects are extended (galaxies) not point sources — matching is harder
- Cross-matching CMB data with galaxy catalogs requires different approaches (pixel-based)
- Always preserve original IDs from both catalogs
