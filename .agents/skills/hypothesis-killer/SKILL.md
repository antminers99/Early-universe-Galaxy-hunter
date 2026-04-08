---
name: hypothesis-killer
description: Actively try to destroy a hypothesis we believe in. Use when we have a promising finding and need to stress-test it. If the hypothesis survives, it becomes stronger.
---

# Hypothesis Killer

## Purpose

Try to destroy the hypothesis we like. If it survives, it becomes stronger. If it doesn't, we saved ourselves from a false result.

## When to Use

- We have a hypothesis we're excited about
- Before publishing or sharing any finding
- When we want to be sure we're not fooling ourselves
- As the final validation step

## Process

1. **State the hypothesis clearly**: What exactly are we claiming?
2. **Attack from every angle**:
   - What data would DISPROVE this?
   - What alternative hypothesis predicts the same observation?
   - What assumptions does the hypothesis rely on?
   - What would the strongest critic say?
3. **Design killer tests**:
   - Tests that can definitively rule out the hypothesis
   - Tests using independent data
   - Tests using different methodology
4. **Execute tests honestly**:
   - Don't soften the tests
   - Don't explain away negative results
   - Don't cherry-pick favorable outcomes
5. **Score the hypothesis**

## Killer Test Categories

### Data-based attacks
- Does the result hold in independent datasets?
- Does it hold in different sky regions?
- Does it hold at different epochs?

### Method-based attacks
- Does a different analysis give the same result?
- Is the result sensitive to priors or assumptions?
- Would a blind analysis reproduce it?

### Theory-based attacks
- Does it violate known physics?
- Is it consistent with other observations?
- Does it require unreasonable assumptions?

### Statistical attacks
- Trial factor — how many hypotheses were tested?
- Posterior predictive checks — does the model fit well?
- Cross-validation — does it generalize?

## Output Format

```
## محاولة هدم الفرضية

### الفرضية
[ما نحاول هدمه]

### الهجمات
| الهجمة | النوع | النتيجة | الفرضية صمدت؟ |
|--------|-------|---------|--------------|
| بيانات مستقلة | بيانات | [result] | نعم/لا |
| طريقة مختلفة | منهج | [result] | نعم/لا |
| توافق نظري | نظري | [result] | نعم/لا |
| اختبار إحصائي | إحصائي | [result] | نعم/لا |

### الحكم النهائي
- [ ] الفرضية انهارت — يجب التخلي عنها
- [ ] الفرضية ضعيفة — تحتاج مراجعة كبيرة
- [ ] الفرضية صمدت جزئيًا — تحتاج تعديل
- [ ] الفرضية صمدت — يمكن المتابعة بثقة أكبر

### ملخص
[ما تعلمناه من محاولة الهدم]
```

## AI Notes

- Be genuinely adversarial — don't go easy on hypotheses we like
- The goal is to find truth, not to confirm what we hope for
- A hypothesis that survives honest attacks is worth much more
- Document failed attacks too — they strengthen the case
