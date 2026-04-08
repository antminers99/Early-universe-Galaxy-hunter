---
name: next-step-planner
description: Decide the smartest next step in the research pipeline based on current results, available data, and project goals. Use when an analysis phase is complete and we need to decide what to do next.
---

# Next-Step Planner

## Purpose

Decide the smartest next step based on where we are, what we found, and what data is available.

## When to Use

- After completing an analysis phase
- When results are ambiguous and we need direction
- When multiple paths are available
- When we need to prioritize limited time/resources

## Decision Framework

### 1. Assess Current State
- What have we found so far?
- What's the strength of our findings? (Claim Limiter level)
- What data do we have vs what do we need?
- What skills have we used vs what's pending?

### 2. Evaluate Options
For each possible next step, score:
- **Impact** (1-5): If this succeeds, how important is it?
- **Feasibility** (1-5): Can we actually do this with current resources?
- **Risk** (1-5): How likely is it to fail? (lower = less risk)
- **Dependencies** (1-5): Does it depend on other things finishing first?

Priority score = Impact × Feasibility × (6 - Risk) × (6 - Dependencies)

### 3. Choose Path
- Pick highest-scoring option
- If scores are close, prefer the one that provides the most information
- If stuck, pick the simplest option that teaches us something

## Output Format

```
## تخطيط الخطوة التالية

### الوضع الحالي
[أين نحن الآن]

### الخيارات المتاحة
| الخيار | الأثر | الجدوى | المخاطرة | التبعيات | المجموع |
|--------|-------|--------|----------|----------|---------|

### التوصية
**الخطوة التالية**: [الخيار الأفضل]
**السبب**: [لماذا هذا الخيار]
**المدة المتوقعة**: [تقدير]
**ماذا نحتاج**: [متطلبات]

### الخطة البديلة
إذا لم تنجح الخطوة الأولى: [الخيار البديل]
```

## AI Notes

- Don't always pick the most exciting option — sometimes the boring systematic work is more valuable
- Consider what we learn even from negative results
- Factor in time cost — quick tests before long analyses
- Keep the big picture in mind: we're studying the early universe
