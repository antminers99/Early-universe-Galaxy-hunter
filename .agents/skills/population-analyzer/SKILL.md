---
name: population-analyzer
description: Compare groups of astronomical objects to identify what is normal vs what is different. Use when studying a class of objects to understand their properties and find subpopulations or anomalous members.
---

# Population Analyzer

## Purpose

Compare a group of objects with each other to reveal what's normal and what's different — is the strange thing individual or an entire new type?

## When to Use

- Studying a class of objects (e.g., all galaxies at z > 10)
- Comparing properties across subgroups
- Looking for new subpopulations
- Understanding the distribution of a property

## Process

1. **Define the population**: What objects? What selection criteria?
2. **Measure properties**: List all available properties
3. **Describe the distribution**:
   - Mean, median, mode
   - Standard deviation, IQR
   - Shape: Gaussian? Skewed? Bimodal?
4. **Look for subgroups**:
   - Clustering in property space
   - Bimodality or multimodality
   - Distinct sequences (e.g., red vs blue galaxies)
5. **Compare with expectations**:
   - Do distributions match theoretical predictions?
   - Are there excess or deficit populations?
6. **Identify unusual members**: Connect with Outlier Hunter

## Output Format

```
## تحليل المجموعة

### المجموعة: [description]
### عدد الأجرام: [N]
### معايير الاختيار: [selection criteria]

### توزع الخصائص
| الخاصية | المتوسط | الانحراف المعياري | المدى | الشكل |
|---------|---------|------------------|-------|-------|

### المجموعات الفرعية
[إذا وُجدت مجموعات فرعية]

### المقارنة مع التوقعات
| الخاصية | المرصود | المتوقع | الفرق |
|---------|---------|---------|-------|

### الأعضاء غير العاديين
[قائمة بأهم الأجرام الشاذة — ربط مع Outlier Hunter]

### ملخص
[النتائج الرئيسية]
```

## AI Notes

- Selection effects are critical — understand what's NOT in your sample
- Small samples can be misleading — note sample size limitations
- Comparison samples must be well-defined
- Flag properties where the measurement uncertainty is large relative to the spread
