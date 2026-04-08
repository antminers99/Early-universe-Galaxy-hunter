---
name: visual-inspector
description: Inspect astronomical images for anomalies, unusual features, artifacts, and errors. Use when examining images from telescopes to find unusual objects or verify data quality. Some things are caught by eye before statistics.
---

# Visual Inspector

## Purpose

Inspect images for unusual features, artifacts, anomalies, and errors. Some things are caught by the eye before statistical analysis can find them.

## When to Use

- Examining new telescope images
- Looking for unusual or unexpected objects
- Checking data quality before analysis
- Verifying detections from automated pipelines

## What to Look For

### Anomalies (potentially interesting)
- Unusual colors compared to surrounding objects
- Unexpected shapes or morphologies
- Objects that don't match known categories
- Gravitational lensing arcs
- Tidal tails or merger signatures

### Artifacts (not real — data problems)
- Cosmic ray hits (sharp bright spots)
- Satellite trails (straight bright lines)
- Diffraction spikes from bright stars
- Detector edge effects
- Persistence from previous exposures (JWST IR)
- Hot/dead pixels

### Quality Issues
- Background gradients
- Flat-fielding problems
- Astrometry errors (misaligned layers)
- PSF problems (elongated or asymmetric stars)

## Process

1. **Overview**: Look at the full image at low zoom
2. **Check background**: Is it uniform? Any gradients?
3. **Check bright sources**: Stars look right? Diffraction spikes normal?
4. **Scan systematically**: Go through the image section by section
5. **Flag items**: Mark anything unusual with coordinates
6. **Classify**: Anomaly vs artifact vs quality issue

## Output Format

```
## تقرير الفحص البصري

### الصورة: [filename]
- الأداة: [instrument]
- المرشح: [filter]
- الحجم: [dimensions]

### الأشياء الملاحظة
| النوع | الإحداثيات | الوصف | التصنيف |
|-------|-----------|-------|---------|
| شاذ | RA, Dec | [description] | anomaly |
| قطعة أثرية | RA, Dec | [description] | artifact |

### جودة الصورة العامة
- الخلفية: [uniform/gradient/noisy]
- النجوم: [normal/elongated/artifacts]
- التقييم: [good/acceptable/poor]

### توصيات
[ما يجب متابعته]
```

## AI Notes

- AI vision can help flag candidates but human review is essential for unusual objects
- Always compare with images in other bands/filters
- Context matters — what's unusual in one field may be common in another
- Document the inspection even if nothing unusual is found
