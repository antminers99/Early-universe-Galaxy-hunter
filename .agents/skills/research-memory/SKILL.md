---
name: research-memory
description: Remember everything tried, failed, and succeeded in the research process. Use to maintain a persistent log of all research activities, decisions, and outcomes across sessions.
---

# Research Memory

## Purpose

Remember everything we tried, what failed, and what succeeded. This is the project's long-term memory.

## When to Use

- After every analysis session
- When starting a new session (read previous memory)
- When deciding next steps
- When someone asks "what have we tried?"

## Memory Structure

Maintain a research log at `data/research_log.json`:

```json
{
  "project": "Early Universe Research",
  "entries": [
    {
      "id": "entry_001",
      "date": "2025-04-08",
      "type": "analysis|discovery|failure|decision|note",
      "title": "Brief title",
      "description": "What was done",
      "data_used": ["dataset names"],
      "tools_used": ["skill names"],
      "result": "What happened",
      "outcome": "success|partial|failure|inconclusive",
      "lessons": "What we learned",
      "next_steps": "What to do next",
      "related_entries": ["entry_XXX"]
    }
  ]
}
```

## Output Format

```
## ذاكرة البحث

### آخر الأنشطة
[أحدث 5 إدخالات]

### ملخص التقدم
- المحاولات الناجحة: X
- المحاولات الفاشلة: X
- قيد التحقيق: X

### أهم الدروس المستفادة
[أهم 3 دروس]

### القرارات المعلقة
[ما يحتاج قرار]
```
