---
name: robustness-checker
description: Re-test results using different methods, parameters, and subsets to verify they are robust. Use when a result looks promising and needs to be stress-tested. If a result collapses with small changes, it is likely weak.
---

# Robustness Checker

## Purpose

Re-test results with different methods. If a result collapses with small changes, it's probably weak.

## When to Use

- A pattern or outlier passed initial statistical testing
- Before writing up any finding
- When results seem fragile or marginal
- When different team members get different results

## Robustness Tests

### 1. Parameter Variation
- Change analysis parameters by ±10%, ±20%, ±50%
- Does the result persist? At what point does it break?
- Which parameters is the result most sensitive to?

### 2. Data Subset Testing
- Split data in half randomly — does result appear in both halves?
- Remove 10% of data randomly — does result persist?
- Use only the highest-quality data subset
- Test different sky regions separately

### 3. Method Variation
- Apply a completely different analysis method
- If using binned analysis, try unbinned
- If using frequentist stats, try Bayesian
- If using one correlation measure, try another

### 4. Known Signal Injection
- Inject a known fake signal into the data
- Can our pipeline recover it correctly?
- At what strength is it detectable?
- Does our method introduce false signals?

### 5. Null Testing
- Randomize/shuffle the data
- Run the same analysis on randomized data
- How often does a "result" appear by chance?

## Output Format

```
## فحص المتانة

### النتيجة المفحوصة
[ما نختبره]

### الاختبارات
| الاختبار | الطريقة | النتيجة تصمد؟ | التفاصيل |
|----------|---------|--------------|----------|
| تغيير المعاملات | ±20% | نعم/لا | [details] |
| تقسيم البيانات | نصفين | نعم/لا | [details] |
| طريقة مختلفة | [method] | نعم/لا | [details] |
| حقن إشارة | [strength] | نعم/لا | [details] |
| اختبار عدمي | تبديل عشوائي | نعم/لا | [details] |

### الحكم
- [ ] متين جدًا — يصمد تحت كل الاختبارات
- [ ] متين بشكل معقول — يصمد تحت معظم الاختبارات
- [ ] هش — ينهار مع تغييرات صغيرة
- [ ] غير مؤكد — يحتاج مزيد من الاختبارات

### ملاحظات
[أي نقاط ضعف محددة]
```

## AI Notes

- Automate as many robustness tests as possible
- Document all parameter ranges tested
- A robust result is more trustworthy but not necessarily correct
- Fragility in one specific test might reveal something interesting about the data
