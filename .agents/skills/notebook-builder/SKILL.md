---
name: notebook-builder
description: Build organized analysis notebooks that combine code, results, and explanations. Use when creating structured analysis documents that show the full pipeline from data to results.
---

# Notebook Builder

## Purpose

Build organized analysis notebooks that combine code, results, and explanations in a structured, reproducible format.

## When to Use

- Creating a new analysis pipeline
- Documenting a complex analysis step-by-step
- Building a shareable analysis record
- Combining multiple analysis steps into one document

## Notebook Structure

```
# عنوان التحليل

## 1. الهدف
[ما نحاول تحقيقه]

## 2. البيانات
[ما نستخدمه — المصادر والملفات]

## 3. المنهجية
[ماذا سنفعل — الخطوات]

## 4. التحليل
### 4.1 [خطوة 1]
[الكود والنتائج]

### 4.2 [خطوة 2]
[الكود والنتائج]

## 5. النتائج
[ملخص ما وجدناه]

## 6. المناقشة
[ماذا تعني النتائج]

## 7. الخطوات التالية
[ماذا بعد]

## 8. الملاحق
[تفاصيل إضافية]
```

## Rules

- Every code cell must have a comment explaining what it does
- Every figure must have a caption
- Every result must have context
- Link to data sources and reproducibility info
- Include version information for all packages used
