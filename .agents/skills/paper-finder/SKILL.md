---
name: paper-finder
description: Find and collect key research papers related to a data source or research question. Use when the user needs to find relevant literature, survey papers, or foundational references for their cosmic research.
---

# Paper Finder

## Purpose

Collect the most important research papers related to each data source or research question, so we don't duplicate work others have already done.

## When to Use

- Starting research on a new topic or data source
- Need foundational references for a methodology
- Want to know what's already been discovered in a specific area
- Looking for techniques others have used on similar data

## Process

1. **Define the search scope**: What data source, object type, or question?
2. **Search strategy**:
   - Search arXiv (astro-ph.CO, astro-ph.GA, astro-ph.IM)
   - Search NASA ADS (ui.adsabs.harvard.edu)
   - Check data release papers (every major survey has key papers)
   - Look for review articles on the topic
3. **Prioritize papers by**:
   - Data release papers (describe the dataset itself)
   - Methodological papers (how to analyze this type of data)
   - Key result papers (what others found)
   - Review papers (overview of the field)
4. **For each paper, record**:
   - Title, authors, year
   - arXiv ID or DOI
   - Brief summary (1-2 sentences)
   - Relevance to our question
   - Category: data-release / methodology / result / review

## Output Format

```
## الأوراق البحثية - [الموضوع]

### أوراق إطلاق البيانات
1. **[Title]** (Authors, Year) — arXiv:XXXX.XXXXX
   الملخص: [1-2 sentences in Arabic]

### أوراق المنهجية
[same format]

### أوراق النتائج الرئيسية
[same format]

### مراجعات شاملة
[same format]

### ملخص
- عدد الأوراق: X
- أهم ورقة للبدء: [title]
- الفجوة المعرفية: [ما لم يُدرس بعد]
```

## Key Search Resources

- **arXiv**: arxiv.org/list/astro-ph.CO/recent
- **NASA ADS**: ui.adsabs.harvard.edu
- **Google Scholar**: scholar.google.com
- **Semantic Scholar**: semanticscholar.org
- **INSPIRE-HEP**: inspirehep.net (for cosmology/particle)

## AI Notes

- Focus on papers from the last 5 years unless classics are needed
- Always include the original data release paper for any dataset
- Flag if a paper has been superseded by newer work
- Note citation count as a rough quality indicator
