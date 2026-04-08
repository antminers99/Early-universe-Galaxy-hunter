---
name: data-cleaner
description: Clean astronomical data by removing duplicates, handling missing values, fixing obvious errors, and standardizing columns. Use when data needs to be prepared before analysis. Many false results come from dirty data.
---

# Data Cleaner

## Purpose

Clean data to remove noise and errors that could produce false results. Many supposed "discoveries" turn out to be artifacts of dirty data.

## When to Use

- Before any analysis on a new dataset
- After merging data from multiple sources
- When results seem suspicious and data quality is in question
- After downloading raw data

## Cleaning Steps

### 1. Duplicate Detection
- Check for exact row duplicates
- Check for near-duplicates (same coordinates, slightly different values)
- Flag duplicates from overlapping survey regions

### 2. Missing Values
- Identify columns with missing data
- Determine if missing = not observed vs. below detection limit
- Decide strategy: remove rows, impute, or flag
- Never silently fill missing values without documenting

### 3. Obvious Errors
- Values outside physical range (negative flux, redshift > 20, etc.)
- Coordinate errors (RA > 360, Dec > 90)
- Magnitude/flux inconsistencies
- Timestamp errors

### 4. Column Standardization
- Unify column names across datasets
- Convert units to common system
- Standardize coordinate systems (all to ICRS J2000)
- Standardize redshift conventions (heliocentric vs. CMB frame)

### 5. Quality Flags
- Respect existing quality flags from surveys
- Create new quality flags for issues found
- Document what each flag means

## Output Format

```
## تقرير تنظيف البيانات

### الملف: [filename]

### المشاكل المكتشفة
| النوع | العدد | الإجراء |
|-------|-------|---------|
| مكرر | XX | حذف |
| ناقص | XX | تعليم |
| خطأ واضح | XX | حذف |
| أعمدة غير موحدة | XX | تحويل |

### قبل التنظيف
- عدد الصفوف: X
- عدد الأعمدة: X

### بعد التنظيف
- عدد الصفوف: X
- عدد الأعمدة: X
- الصفوف المحذوفة: X (X%)

### تفاصيل التنظيف
[ماذا تم عمله بالتحديد]

### تحذيرات
[أي مشاكل لم تُحل أو تحتاج مراجعة يدوية]
```

## AI Notes

- NEVER modify raw data files — always work on copies
- Document every cleaning step for reproducibility
- Be conservative: better to flag and review than to silently remove
- Some "outliers" might be real discoveries — don't clean them away
- Flag any cleaning decision that could affect scientific results
