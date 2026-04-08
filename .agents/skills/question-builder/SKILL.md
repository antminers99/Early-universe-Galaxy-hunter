---
name: question-builder
description: Convert broad research ideas into specific, testable scientific questions. Use when the user has a big idea but needs to narrow it down to something that can actually be investigated with available data. One of the top 3 core skills for this project.
---

# Question Builder

## Purpose

Transform a big, vague idea into a small, specific question that can be tested with available data. Discovery starts from a clear question.

## Why This Is Core

This is one of the 3 most important skills in the project. Without a clear question:
- We don't know what data to download
- We don't know what analysis to run
- We can't tell if we found something or not

## When to Use

- User has a broad research interest ("I want to study the early universe")
- Starting a new investigation
- A previous question led nowhere and we need to pivot
- We found something interesting and need to formulate a follow-up question

## Process

1. **Start with the broad idea**: What is the user interested in?
2. **Identify available data**: What datasets can we actually access?
3. **Narrow the scope**:
   - What specific objects? (galaxies, quasars, CMB patches)
   - What specific property? (luminosity, redshift, morphology, spectrum)
   - What specific anomaly or pattern? (unexpected, missing, excess)
   - What specific epoch? (z > 10, z = 6-8, recombination)
4. **Formulate the question**: Must be answerable with "yes/partially/no" or a measurable quantity
5. **Check feasibility**:
   - Is the data available and accessible?
   - Is the analysis doable with our tools?
   - Has this exact question been answered before?

## Question Quality Checklist

A good question must be:
- [ ] **Specific**: Not "what happened at the beginning" but "is there X in dataset Y"
- [ ] **Testable**: Can be answered with available data
- [ ] **Novel**: Not already fully answered (check with Paper Finder)
- [ ] **Bounded**: Has a clear scope (which data, which objects, which property)
- [ ] **Falsifiable**: Can be proven wrong

## Examples

### Bad → Good Transformations

**Bad**: "نريد نكتشف بداية الكون"
**Good**: "هل يوجد نمط غير متوقع في توزع أوائل المجرات عند z > 10 في داتا JWST?"

**Bad**: "نريد نفهم CMB"
**Good**: "هل هناك إشارة شاذة في خرائط بلانك عند المقاييس الزاوية الكبيرة لم تُفسَّر بعد؟"

**Bad**: "ندرس الانزياح الأحمر"
**Good**: "هل توزع الانزياح الأحمر الضوئي لمجرات DESI DR1 يتطابق مع التوقعات النظرية عند z > 2؟"

## Output Format

```
## بناء السؤال البحثي

### الفكرة الأصلية
[ما قاله المستخدم]

### السؤال المقترح
[السؤال المحدد والقابل للاختبار]

### لماذا هذا السؤال؟
- البيانات المتاحة: [أي datasets]
- الأدوات المطلوبة: [أي تحليلات]
- ماذا نتوقع أن نجد: [النتيجة المتوقعة]
- ماذا لو وجدنا شيء مختلف: [لماذا يكون مهمًا]

### فحص الجودة
- محدد: نعم/لا
- قابل للاختبار: نعم/لا
- جديد: نعم/لا
- محدود النطاق: نعم/لا
- قابل للدحض: نعم/لا

### أسئلة بديلة
1. [سؤال بديل 1]
2. [سؤال بديل 2]
```

## AI Notes

- Always propose 2-3 alternative questions, not just one
- Be honest if a question is too ambitious for available data
- Flag questions that require expert human judgment
- Connect each question to specific available datasets
