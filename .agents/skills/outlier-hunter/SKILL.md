---
name: outlier-hunter
description: Find objects or measurements that deviate significantly from the norm. Use when searching for unusual objects that could represent new discoveries. One of the top 3 core skills - new discoveries often start from something that doesn't look like the rest.
---

# Outlier Hunter

## Purpose

Find things that are outside the norm. New discoveries very often start from something that "doesn't look like the rest."

## Why This Is Core

This is one of the 3 most important skills in the project. The unusual object, the unexpected measurement, the thing that doesn't fit — that's often where discovery lives.

## When to Use

- After initial data exploration
- Looking for unusual objects in a catalog
- Searching for unexpected measurements
- Validating that automated classifications haven't missed anything

## Types of Outliers

### Photometric Outliers
- Unusual colors (very red, very blue, unexpected)
- Extreme brightness (too bright or too faint for category)
- Unusual variability patterns

### Spectroscopic Outliers
- Unusual emission/absorption features
- Extreme redshifts
- Unclassifiable spectra
- Unexpected line ratios

### Morphological Outliers
- Unusual shapes
- Unexpected sizes
- Strange spatial profiles

### Statistical Outliers
- Points far from the mean in any distribution
- Objects in unexpected regions of parameter space
- Rare combinations of properties

## Process

1. **Define "normal"**: What does the typical object look like?
   - Use the bulk of the data to establish baseline
   - Calculate mean, median, standard deviation
   - Build reference distributions
2. **Identify deviations**:
   - sigma-clipping (>3σ, >5σ)
   - Isolation forests
   - Local outlier factor
   - Mahalanobis distance (multi-dimensional)
3. **Classify outliers**:
   - **Genuine**: Real astronomical object with unusual properties
   - **Artifact**: Data problem, instrumental effect
   - **Error**: Measurement or processing error
   - **Unknown**: Needs further investigation
4. **Prioritize**:
   - How unusual is it? (how many sigma)
   - Is it in multiple datasets? (cross-match)
   - Is it a known type of outlier?
   - Could it be scientifically interesting?

## Output Format

```
## صيد الشواذ

### البيانات: [dataset]
### العينة: [N] أجرام

### الشواذ المكتشفة
| الجرم | الخاصية الشاذة | الانحراف | التصنيف | الأولوية |
|-------|----------------|----------|---------|----------|

### تفاصيل الأجرام ذات الأولوية العالية
[لكل جرم مهم: وصف تفصيلي]

### ملخص
- عدد الشواذ: X من أصل Y (X%)
- حقيقية محتملة: X
- قطع أثرية: X
- تحتاج مراجعة: X

### الخطوة التالية
[ماذا نفعل مع الشواذ المكتشفة — ربط مع Bias Checker]
```

## Critical Warning

**Not every outlier is a discovery.** Most outliers are:
- Data artifacts (~60%)
- Known types of unusual objects (~25%)
- Measurement errors (~10%)
- Potentially interesting (~5%)

Always run through Bias Checker and Alternative Explanation Finder before getting excited.

## AI Notes

- AI is excellent at finding outliers in large datasets — this is a strong use case
- But AI should NOT interpret what the outlier means — that needs domain expertise
- Always cross-check outliers against known artifact catalogs
- Save ALL outliers, even those classified as artifacts — sometimes we're wrong about classifications
