# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.

## Project Purpose

Cosmic early universe research platform. The project catalogs astronomical data sources and implements a pipeline of research skills for analyzing early universe data (JWST, CMB, ALMA, Euclid, DESI, SDSS, HERA, GWOSC).

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)
- **Frontend**: React + Vite + Tailwind CSS v4 + shadcn/ui + Recharts
- **UI Direction**: LTR (English)
- **Communication**: Arabic (Levantine dialect) in chat only — app UI is always English

## Artifacts

- **data-app** (`artifacts/data-app`): Cosmic Data Catalog — interactive catalog of early universe data sources with sizes, priorities, and quick-start guide. Served at `/`. Pages: Data Catalog (`/`), Research Plan (`/research`), Download Center (`/downloads`), Visual Inspection (`/inspection`).
  - **JWST Cutouts**: 525 local PNG cutouts (60×60 px, 30 mas/px, 1.8"×1.8") from JADES DR5 mosaics (UCSC). 175 per stretch mode (asinh/sqrt/linear). Naming: `{field_tag}_{id}_{filter}.png` (asinh), `_sqrt.png`, `_linear.png`. 173/175 have real data, 2 empty (GOODS-N edge coverage). Downloaded via HTTP range requests with proper PC-matrix WCS (`scripts/download_cutouts.py`).
  - **Debug Mode UI**: Inspection page (`/inspection`) has toggleable debug mode with: SVG crosshair overlay, per-band PSF FWHM circle (red dashed), source FWHM circle (green solid), angular scale bar (0.2"), stretch toggle (asinh/sqrt/linear), metadata panel, and pipeline validation results panel.
  - **Pipeline Validation**: 3 numerical tests passed on 5 test sources: center consistency (4/5 PASS), band mapping (5/5 PASS), point-source compactness (3/3 PASS). Report: `data/research/pipeline_validation_report_v1.json`.

## Active Research Goals

### Goal 1: Strange Early Galaxies in JWST Public Data
- **Question**: "Are there galaxies at z > 6 in JWST public catalogs (JADES DR5, CEERS, UNCOVER, COSMOS-Web) with anomalous photometric/morphological properties compared to theoretical expectations?"
- **Anomaly types**: Too bright, too red, too compact, too mature for their age
- **Data sources**: JADES DR5 (start here), CEERS, UNCOVER, COSMOS2025, GLASS-JWST
- **External validation**: Euclid Q1, DESI DR1 (later stage)
- **Plan file**: `data/research/goal-01-plan.md`
- **Claim level**: Initial signal only — no discovery claims
- **5 steps**: Download catalogs → Clean/filter z>6 → Hunt outliers → Kill hypotheses → External cross-match
- **Progress tracking**: After completing any step, update status in `research-plan.ts`, update `goal-01-plan.md`, and use `research-progress` skill

## Research Skills Pipeline (26 skills, 4 phases)

### Phase 1 — Foundation (Skills 1-8)
1. **Source Finder** — Find all important data sources from the web
2. **Paper Finder** — Collect key research papers related to each data source or question
3. **Paper Screener** — Classify papers: very important / useful / weak / outdated
4. **Question Builder** — Convert big ideas into small testable questions
5. **Download Manager** — Download, organize, and store data with clear naming
6. **Metadata Reader** — Understand each file: origin, type, instrument used
7. **Data Cleaner** — Clean data: duplicates, missing values, obvious errors, inconsistent columns
8. **Reproducibility Builder** — Make every step reproducible from scratch

### Phase 2 — Analysis (Skills 9-14)
9. **Catalog Cross-Matcher** — Link same object across multiple data sources
10. **Visual Inspector** — Inspect images for anomalies, unusual colors, shapes, errors
11. **Spectra Reader** — Read spectra and extract basic info (AI-assisted but needs human review for sensitive interpretation)
12. **Pattern Finder** — Detect recurring patterns not easily visible
13. **Outlier Hunter** — Find things outside the norm
14. **Population Analyzer** — Compare groups of objects to identify what's normal vs different

### Phase 3 — Validation (Skills 15-20)
15. **Bias Checker** — Check if result is caused by observation method, instrument, sample selection, or data gaps
16. **Statistical Tester** — Determine if result is strong or just coincidence (needs manual review for sensitive analyses)
17. **Robustness Checker** — Re-test with different methods
18. **Alternative Explanation Finder** — Search for ordinary explanations before claiming novelty
19. **Hypothesis Killer** — Try to destroy the hypothesis we like
20. **Claim Limiter** — Calibrate language: initial signal / probability / strong result (not "confirmed discovery")

### Phase 4 — Documentation (Skills 21-26)
21. **Research Memory** — Remember everything tried, failed, and succeeded
22. **Result Summarizer** — Summarize each phase in simple language
23. **Figure Builder** — Create clear visualizations
24. **Notebook Builder** — Build organized analysis notebooks
25. **Report Writer** — Write clean reports
26. **Next-Step Planner** — Decide smartest next step

### Priority Start (first 10 skills to build)
Source Finder, Paper Finder, Paper Screener, Question Builder, Download Manager, Metadata Reader, Data Cleaner, Catalog Cross-Matcher, Outlier Hunter, Bias Checker

### Top 3 Core Skills
- **Question Builder** — clear question
- **Outlier Hunter** — something strange
- **Bias Checker** — verify if real or deception

### AI Trust Guidelines
AI is excellent at: data collection, paper organization, initial cleaning, code writing, pattern searching.
AI should NOT be trusted alone for: very sensitive interpretation, discovery announcements, precise spectral analysis, complex statistical testing without review.

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
