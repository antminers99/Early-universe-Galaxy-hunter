---
name: alternative-explanation-finder
description: Search for ordinary explanations before claiming something is new or unusual. Use before making any discovery claim. This protects the project from premature conclusions.
---

# Alternative Explanation Finder

## Purpose

Search for every ordinary explanation before saying something is new. This protects the project from jumping too fast to exciting but wrong conclusions.

## When to Use

- Before making any discovery claim
- When an outlier or pattern seems scientifically interesting
- When results are unexpected
- As a required step before writing up findings

## Process

1. **State the observation**: What did we see?
2. **List known explanations** (most mundane first):
   - Instrumental artifact
   - Data processing error
   - Known astrophysical phenomenon
   - Selection effect or bias
   - Statistical fluctuation
3. **For each explanation, assess**:
   - Can it fully explain what we see?
   - Can it partially explain it?
   - What evidence rules it out?
4. **Search literature**: Has someone seen this before?
5. **Only after exhausting alternatives**: Consider novel explanation

## The Hierarchy of Explanations (from most to least likely)

1. **Bug in the code** — Always check first
2. **Data artifact** — Instrument, calibration, processing
3. **Known phenomenon** — Something well-understood we didn't recognize
4. **Statistical fluke** — Random chance in a large dataset
5. **Selection effect** — Our sample is biased
6. **Known but rare phenomenon** — Uncommon but documented
7. **New manifestation of known physics** — Known physics in new context
8. **Genuinely new phenomenon** — Only if ALL above are ruled out

## Output Format

```
## البحث عن تفسيرات بديلة

### الملاحظة
[ما رأيناه]

### التفسيرات المحتملة
| التفسير | النوع | ممكن؟ | تم استبعاده؟ | الدليل |
|---------|-------|-------|-------------|--------|
| خطأ في الكود | تقني | نعم/لا | نعم/لا | [evidence] |
| قطعة أثرية | بيانات | نعم/لا | نعم/لا | [evidence] |
| ظاهرة معروفة | فيزيائي | نعم/لا | نعم/لا | [evidence] |
| صدفة إحصائية | إحصائي | نعم/لا | نعم/لا | [evidence] |
| تأثير اختيار | منهجي | نعم/لا | نعم/لا | [evidence] |

### التفسيرات المستبعدة
[ماذا استبعدنا ولماذا]

### التفسيرات المتبقية
[ما لم نستطع استبعاده]

### الحكم
- [ ] مفسَّر بالكامل بظاهرة معروفة
- [ ] مفسَّر جزئيًا — يحتاج مزيد من البحث
- [ ] غير مفسَّر — يستحق المتابعة بحذر
```

## AI Notes

- AI is good at systematically checking known explanations
- AI might miss novel explanations — brainstorm with the team
- The most exciting findings are often the hardest to explain ordinarily
- Document ALL alternatives considered, even silly ones — thoroughness matters
