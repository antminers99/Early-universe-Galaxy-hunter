---
name: paper-screener
description: Screen and classify research papers by importance and relevance. Use when the user has a list of papers and needs to prioritize which ones to read first, or to filter out weak/outdated papers.
---

# Paper Screener

## Purpose

Sort research papers into priority categories so we don't waste time on hundreds of papers — focus on what matters most.

## When to Use

- After Paper Finder returns a list of papers
- User has a large reading list to prioritize
- Need to decide which papers to read in depth vs skim vs skip

## Classification Categories

### مهم جدًا (Critical)
- Directly answers our research question
- Introduces the dataset we're using
- Presents methodology we need to apply
- Contains results we must compare against
- Recent (last 2-3 years) and highly cited

### مفيد (Useful)
- Related but not directly answering our question
- Contains partial methods we can adapt
- Provides context or background
- Moderately cited, reasonably recent

### ضعيف (Weak)
- Tangentially related
- Uses outdated methods or data
- Low citation count with no unique insight
- Superseded by newer work

### قديم (Outdated)
- Results have been replaced by newer data
- Methods have been improved significantly
- Data used is no longer the best available
- Still useful for historical context only

## Screening Criteria

1. **Relevance** (0-5): How directly related to our question?
2. **Recency** (0-5): How recent? Newer data releases matter more
3. **Methodology** (0-5): Is the approach sound and applicable?
4. **Impact** (0-5): Citation count, journal quality
5. **Data quality** (0-5): Does it use the best available data?

Total score: sum / 25 → percentage

- 80-100%: مهم جدًا
- 50-79%: مفيد
- 25-49%: ضعيف
- 0-24%: قديم

## Output Format

```
## فرز الأوراق البحثية

### مهم جدًا (يجب قراءته)
1. **[Title]** — النقاط: XX/25
   السبب: [لماذا مهم]

### مفيد (يستحق القراءة)
[same format]

### ضعيف (للاطلاع فقط)
[same format]

### قديم (للسياق التاريخي)
[same format]

### التوصية
ابدأ بقراءة: [top 3 papers]
```

## AI Notes

- Be honest about limitations — don't inflate importance
- Flag papers where AI cannot fully assess quality (e.g., novel statistical methods)
- Note if a paper is controversial or has been challenged
