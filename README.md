# Food & Sales Budget Variance — Executive Dashboard

An interactive, **self-contained** executive dashboard for Sugarland Petroleum's monthly
Food & Sales Budget Variance report across four stores (Mesa 0008, Polo 0025,
Woodridge 0028, Dilley 0062).

**Live demo:** _(added after deploy)_

## Highlights

- **Single HTML file** — inline SVG charts + vanilla JavaScript. No frameworks, no CDN,
  no build step. Opens offline in any browser.
- **7 views** via a sticky top nav: Overview, four per-store tabs, Trends, and Data.
- **5 color themes** + dark mode, a month selector, hover tooltips, CSV export, print/PDF
  layout, and a Download-Excel button.
- **Fully traceable data** — every figure is cross-checked against source reports
  (Weighted Average, Retail Dept Summary, Cost INIR, hourly sales, customer counts,
  speed-of-service) by an automated verifier before the dashboard is built.

## What's in this repo

| Path | Purpose |
|------|---------|
| `index.html` | The complete dashboard (this is the whole app). |
| `02_Excel_Report/` | The source workbook backing the "Download Excel" button. |
| `vercel.json` | Static hosting config. |

## Run locally

Just open `index.html` in a browser — that's it. Or serve statically:

```bash
python -m http.server 8000   # then visit http://localhost:8000
```

## Tech

Pure HTML/CSS/JS. Charts are hand-rolled inline SVG (donuts, bars, gauges, trend lines).
Client-side hash routing (`#0008`, `#trends`, …). Theme + month state in vanilla JS.

---

Prepared by **Furqan Ali** — Senior AI Engineer.
