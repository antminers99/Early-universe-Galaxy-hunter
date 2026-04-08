---
name: statistical-tester
description: Determine if a result is statistically significant or just coincidence. Use after finding patterns or outliers to assess their strength. AI is good at computation but sensitive analyses need manual methodology review.
---

# Statistical Tester

## Purpose

Tell us whether a result is strong or just coincidence, so we don't get fooled by phantom patterns.

## When to Use

- After Pattern Finder or Outlier Hunter reports something
- Before making any quantitative claim
- When comparing two populations
- When testing a specific hypothesis

## Common Tests

### For Distributions
- **KS test**: Are two distributions different?
- **Anderson-Darling**: Is data consistent with a model?
- **Chi-squared**: Does observed match expected?

### For Correlations
- **Pearson r**: Linear correlation
- **Spearman rho**: Monotonic correlation (rank-based)
- **Kendall tau**: Ordinal association

### For Significance
- **p-value**: Probability of seeing this result by chance
- **sigma level**: Standard deviations from null (3σ = evidence, 5σ = discovery in physics)
- **Bayes factor**: Relative evidence for two hypotheses

### For Multiple Testing
- **Bonferroni correction**: Divide α by number of tests
- **False Discovery Rate (FDR)**: Control fraction of false positives
- **Look-elsewhere effect**: Account for searching many locations

## Significance Standards in Astronomy

| Level | Sigma | p-value | Meaning |
|-------|-------|---------|---------|
| Hint | 2σ | 0.05 | إشارة أولية |
| Evidence | 3σ | 0.003 | دليل يستحق المتابعة |
| Strong evidence | 4σ | 6×10⁻⁵ | دليل قوي |
| Discovery | 5σ | 6×10⁻⁷ | اكتشاف (معيار فيزياء الجسيمات) |

## Output Format

```
## الاختبار الإحصائي

### الفرضية
- H₀ (العدم): [ما نحاول دحضه]
- H₁ (البديلة): [ما نريد إثباته]

### الاختبار المستخدم
- النوع: [اسم الاختبار]
- لماذا هذا الاختبار: [السبب]

### النتائج
| الإحصاء | القيمة | p-value | المستوى |
|---------|--------|---------|---------|

### تصحيح الاختبارات المتعددة
- عدد الاختبارات: [N]
- طريقة التصحيح: [Bonferroni/FDR]
- p-value بعد التصحيح: [value]

### الحكم
[إشارة أولية / دليل / دليل قوي / اكتشاف / غير دال]

### تحذيرات
[أي افتراضات قد تكون مكسورة]
```

## AI Trust Warning

AI is excellent at **computation** here — calculating statistics, running tests, handling large datasets.

But for **sensitive analyses**, human review of methodology is essential:
- Are the test assumptions met? (normality, independence, etc.)
- Is the test appropriate for this type of data?
- Are there hidden dependencies in the data?
- Is the multiple testing correction adequate?
