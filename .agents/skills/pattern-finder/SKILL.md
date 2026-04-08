---
name: pattern-finder
description: Detect recurring patterns in astronomical data that are not easily visible. Use when searching for hidden structures, correlations, or regularities in large datasets that might indicate new phenomena.
---

# Pattern Finder

## Purpose

Detect recurring patterns that don't appear easily — we're looking for things hidden inside massive amounts of data.

## When to Use

- Searching for structure in spatial distributions
- Looking for periodicities in time series
- Finding correlations between properties
- Detecting clustering or grouping

## Types of Patterns

### Spatial Patterns
- Clustering of objects on the sky
- Voids or underdensities
- Filamentary structures
- Alignment of galaxy orientations

### Temporal Patterns
- Periodic signals
- Transient events
- Evolution trends with redshift

### Property Correlations
- Luminosity-mass relations
- Color-magnitude diagrams
- Size-redshift relations
- Unexpected correlations between unrelated properties

### Statistical Patterns
- Non-Gaussian distributions
- Excess power at specific scales
- Anomalous two-point correlations

## Process

1. **Define what we're looking for**: Guided by the research question
2. **Choose appropriate method**:
   - Correlation functions for spatial clustering
   - Fourier/wavelet analysis for periodicities
   - PCA/t-SNE for high-dimensional patterns
   - KDE for density estimation
3. **Apply method and assess significance**:
   - Compare against null hypothesis (random/expected)
   - Use proper statistical tests (link to Statistical Tester)
4. **Verify pattern is real**:
   - Check against known artifacts and biases (link to Bias Checker)
   - Test robustness (link to Robustness Checker)
5. **Document finding**

## Output Format

```
## البحث عن أنماط

### البيانات: [dataset]
### السؤال: [ما نبحث عنه]

### الأنماط المكتشفة
| النمط | النوع | القوة | الدلالة الإحصائية |
|-------|-------|-------|------------------|

### التفاصيل
[وصف كل نمط]

### فحص المصداقية
- هل ممكن يكون انحياز؟ [نعم/لا — التفاصيل]
- هل هو معروف سابقًا؟ [نعم/لا]
- هل هو متين؟ [نعم/لا — بأي طريقة فحصناه]

### التوصية
[ماذا نفعل بهذا النمط]
```

## AI Notes

- Not every pattern is real — always check significance
- The human eye is great at seeing patterns that don't exist (pareidolia)
- Multiple testing correction is essential when searching for many patterns
- Always compare against randomized/shuffled data
