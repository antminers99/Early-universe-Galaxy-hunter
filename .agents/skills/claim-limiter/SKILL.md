---
name: claim-limiter
description: Calibrate the language of results to match their actual strength. Use before writing any finding to ensure we say 'initial signal' or 'possible' instead of 'confirmed discovery'. Keeps us honest.
---

# Claim Limiter

## Purpose

Calibrate the language of results: initial signal, possibility, strong result — never "confirmed discovery" too quickly. This keeps us honest.

## When to Use

- Before writing up any finding
- When formulating conclusions
- When the user asks "did we discover something?"
- When preparing any communication about results

## Claim Strength Ladder

### Level 1: إشارة أولية (Initial Signal)
- First detection, not yet verified
- Single dataset, single method
- Marginal statistical significance (2-3σ)
- Language: "نلاحظ إشارة أولية...", "يبدو أن هناك..."
- English: "We note a tentative signal...", "There appears to be..."

### Level 2: ملاحظة مثيرة للاهتمام (Interesting Observation)
- Passed basic bias checks
- Reasonable significance (3-4σ)
- Not yet tested with independent data
- Language: "نكتشف ملاحظة مثيرة...", "البيانات تشير إلى..."
- English: "We find an intriguing...", "The data suggest..."

### Level 3: نتيجة قوية (Strong Result)
- Confirmed in independent data
- Robust across methods
- Known biases accounted for
- High significance (>4σ)
- Language: "نؤكد وجود...", "البيانات تدعم بقوة..."
- English: "We confirm...", "The data strongly support..."

### Level 4: اكتشاف (Discovery)
- Passed ALL validation steps
- Independent replication
- Peer review
- 5σ or equivalent Bayesian evidence
- Language: "نعلن اكتشاف..."
- English: "We report the discovery of..."
- **NEVER reach this level without external validation**

## Forbidden Phrases (until earned)

- "اكتشفنا" — until Level 4
- "نثبت أن" — until Level 3+
- "بالتأكيد" — almost never
- "لأول مرة" — only if literature review confirms
- "ثوري" / "revolutionary" — let others judge

## Required Qualifiers by Level

| Level | Must Include |
|-------|-------------|
| 1 | "أولي", "يحتاج تأكيد", "محتمل" |
| 2 | "يستحق المتابعة", "البيانات تشير", "بعد فحص أولي" |
| 3 | "بعد فحص شامل", "متين", "عبر عدة طرق" |
| 4 | "بعد تحقق مستقل", "بثقة عالية" |

## Output Format

```
## معايرة الادعاء

### النتيجة
[ما وجدناه]

### مستوى الادعاء الحالي
[Level 1/2/3/4]

### التبرير
- الدلالة الإحصائية: [value]
- بيانات مستقلة: [نعم/لا]
- فحص الانحياز: [تم/لم يتم]
- فحص المتانة: [تم/لم يتم]
- تفسيرات بديلة: [مستبعدة/متبقية]

### الصياغة المقترحة
[الجملة المناسبة لمستوى الادعاء]

### ما يلزم للترقية
[ماذا نحتاج لنصل للمستوى التالي]
```

## AI Notes

- AI must NEVER use discovery-level language without explicit human approval
- When in doubt, go DOWN a level, not up
- Excitement about a finding is not evidence for its strength
- The strongest scientists are the most careful with their claims
