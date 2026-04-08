---
name: research-progress
description: Track and update research goal progress. Use after completing any research step or phase to mark it done, record what was accomplished, and update the app UI.
---

# Research Progress Tracker

## Purpose

Keep a persistent record of completed research steps and update the app to reflect current progress. Every time a step or phase is finished, this skill ensures it is marked complete everywhere.

## When to Use

- After completing any step in a research goal (e.g., "Download Catalogs" is done)
- After a major phase milestone (e.g., all Phase 1 steps complete)
- When the user asks about current progress

## Process

### 1. Update the App Data
Edit the step's `status` field in the research plan data file:
- File: `artifacts/data-app/src/data/research-plan.ts`
- Change `status: "pending"` to `status: "done"` for the completed step
- If a step is actively being worked on, set `status: "in-progress"`

### 2. Update the Research Plan Document
Add a completion note to the research plan markdown:
- File: `data/research/goal-01-plan.md`
- Add completion date and summary under the relevant step

### 3. Update Research Memory
Log the completion in the research memory skill:
- What was done
- Key findings or outputs
- Any issues encountered
- What data files were produced

### 4. Restart the App
Restart the data-app workflow so the UI reflects the updated status.

## Step Status Values
- `"pending"` — Not started yet
- `"in-progress"` — Currently being worked on
- `"done"` — Completed

## Example Update Flow

When Step 1 (Download Catalogs) is complete:

1. In `research-plan.ts`, change step 1 status to `"done"`
2. In `goal-01-plan.md`, add: "### Step 1 — Completed [date]. Downloaded X catalogs, Y total rows."
3. Log in research memory
4. Restart data-app workflow

## Checklist Before Marking Done
- [ ] The step's deliverable exists (files, data, analysis)
- [ ] Any code written for this step is saved and reproducible
- [ ] The research plan markdown is updated with results summary
- [ ] The app data file status is updated
- [ ] The app is restarted to show updated status
- [ ] Research memory is updated

## AI Notes
- Never mark a step as done if the work is incomplete
- Always include what was actually produced (files, counts, findings)
- If a step partially succeeded, note what worked and what didn't
- Keep the progress log factual — no speculation about future steps
