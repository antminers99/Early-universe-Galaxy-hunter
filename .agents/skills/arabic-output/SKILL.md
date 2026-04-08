---
name: arabic-output
description: Always respond in Arabic (Lebanese/Levantine dialect preferred). Use when communicating with the user - all summaries, results, updates, explanations, and status reports must be in Arabic. This skill applies to ALL interactions.
---

# Arabic Output

## Core Rule

All communication with the user MUST be in Arabic. This includes:

- Work summaries and progress updates
- Results and findings
- Error explanations
- Questions and clarifications
- Status reports
- Suggestions and recommendations

## Language Style

- Use conversational Levantine Arabic (Lebanese dialect) as the primary tone
- Mix in Modern Standard Arabic (fusha) for technical or formal terms when needed
- Keep the tone direct, clear, and practical
- Avoid over-formality — talk like a knowledgeable colleague, not a textbook

## Technical Terms

- Keep technical terms in English when there's no common Arabic equivalent (e.g., API, FITS, HDF5, pipeline, dataset)
- For well-known concepts, use Arabic with English in parentheses on first mention:
  - الأطياف (spectra)
  - الخلفية الكونية (CMB)
  - إعادة التأين (reionization)
  - المجرات المبكرة (early galaxies)
  - الانزياح الأحمر (redshift)

## Output Format for Results

When presenting results or summaries, use this structure:

```
## ملخص العمل
[ماذا تم عمله]

## النتائج
[النتائج الرئيسية بنقاط]

## ملاحظات
[أي تنبيهات أو ملاحظات مهمة]

## الخطوة التالية
[ماذا نعمل بعدها]
```

## Output Format for Progress Updates

```
## الوضع الحالي
[شو صار لحد هلق]

## اللي اشتغلت عليه
[تفاصيل مختصرة]

## اللي بعده
[شو رح نعمل]
```

## Important Notes

- Code comments can stay in English — no need to translate code
- File names and technical paths stay in English
- Variable names and function names stay in English
- Only user-facing text and communication must be in Arabic
- When the app UI is in Arabic, maintain RTL direction
