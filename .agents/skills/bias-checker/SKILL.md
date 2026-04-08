---
name: bias-checker
description: Check if a result is caused by observation method, instrument, sample selection, or data gaps rather than being a real phenomenon. Use after finding any pattern or outlier. One of the top 3 core skills - many supposed discoveries turn out to be just bias.
---

# Bias Checker

## Purpose

Check if a result is caused by how we observed, what instrument we used, how we selected our sample, or what data we're missing — rather than being a real phenomenon. Many "discoveries" turn out to be just bias.

## Why This Is Core

This is one of the 3 most important skills in the project. It protects us from false discoveries.

## When to Use

- After Pattern Finder finds something
- After Outlier Hunter flags unusual objects
- Before making any claim about a result
- When a result seems "too good to be true"

## Types of Bias

### Observational Bias
- **Malmquist bias**: Brighter objects are easier to detect at large distances
- **Eddington bias**: Measurement noise scatters objects across selection boundaries
- **Aperture bias**: Instrument field of view limits what we see
- **Wavelength bias**: Different instruments see different parts of spectrum

### Selection Bias
- **Target selection**: How were objects chosen for observation?
- **Magnitude limits**: Are we only seeing the brightest ones?
- **Spectroscopic incompleteness**: Not all photometric candidates have spectra
- **Survey footprint**: The sky isn't uniformly covered

### Instrumental Bias
- **Detector sensitivity**: Varies across the focal plane
- **Calibration errors**: Systematic offsets in measurements
- **Resolution limits**: Can't separate close objects
- **Persistence/crosstalk**: Ghost signals from other observations

### Analysis Bias
- **Look-elsewhere effect**: Finding a pattern because we searched everywhere
- **Confirmation bias**: Seeing what we want to see
- **Binning effects**: Results that depend on how data is binned
- **Prior assumptions**: Starting assumptions that shape the result

## Process

1. **State the finding**: What did we find?
2. **For each bias type, ask**:
   - Could this bias produce the observed result?
   - How likely is it?
   - Can we test for it?
3. **Test explicitly**:
   - Inject fake signals to test detection limits
   - Compare with simulations
   - Check different subsets of the data
   - Vary analysis parameters
4. **Verdict**:
   - Bias explains the result → not a real finding
   - Bias partially contributes → need to quantify
   - Bias does not explain it → proceed carefully

## Output Format

```
## فحص الانحياز

### النتيجة المفحوصة
[ما وجدناه]

### فحص كل نوع انحياز
| نوع الانحياز | ممكن؟ | الاحتمال | تم الفحص؟ | النتيجة |
|-------------|-------|----------|-----------|---------|
| رصدي | نعم/لا | عالي/منخفض | نعم/لا | [تفاصيل] |
| اختيار العينة | نعم/لا | عالي/منخفض | نعم/لا | [تفاصيل] |
| الأداة | نعم/لا | عالي/منخفض | نعم/لا | [تفاصيل] |
| التحليل | نعم/لا | عالي/منخفض | نعم/لا | [تفاصيل] |

### الحكم
- [ ] النتيجة مفسرة بالكامل بالانحياز
- [ ] الانحياز يساهم جزئيًا
- [ ] الانحياز لا يفسر النتيجة
- [ ] غير واضح — يحتاج مزيد من الفحص

### التوصية
[ماذا نفعل بعد هذا الفحص]
```

## AI Notes

- AI can systematically check for known biases — this is a good use case
- But AI might miss novel or subtle biases — human review is important for strong claims
- Always document which biases were checked even if none were found
- The absence of detected bias does NOT prove the result is real
