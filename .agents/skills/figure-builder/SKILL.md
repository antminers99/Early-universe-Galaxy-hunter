---
name: figure-builder
description: Create clear scientific visualizations and figures for research results. Use when results need to be presented visually — charts, plots, sky maps, spectra plots, or comparison figures.
---

# Figure Builder

## Purpose

Create clear, publication-quality visualizations for research results.

## When to Use

- Results need visual presentation
- Comparing data across datasets
- Showing spatial distributions on sky maps
- Plotting spectra, light curves, or distributions
- Preparing figures for reports

## Figure Types

### Distribution Plots
- Histograms for property distributions
- KDE plots for smooth distributions
- Box plots for comparing groups

### Correlation Plots
- Scatter plots with error bars
- Color-magnitude diagrams
- Property vs property plots

### Spatial Plots
- Sky maps (RA/Dec)
- HEALPix maps for CMB
- Field-of-view overlays

### Spectral Plots
- Wavelength vs flux with line labels
- Multi-panel spectra comparison
- Residual plots

### Summary Figures
- Multi-panel overview figures
- Before/after comparisons
- Pipeline flowcharts

## Standards

- Clear axis labels with units
- Readable font sizes (min 10pt)
- Color-blind friendly palettes
- Error bars when available
- Legend explaining all symbols
- Title describing what the figure shows
- Arabic labels for user-facing figures, English for publication

## Output Format

```
## الرسومات

### الرسم: [title]
- النوع: [plot type]
- البيانات: [data source]
- الملف: [output path]
- الوصف: [ما يُظهره الرسم]
```
