# Week 14 - Web Scraping & Dashboard: Run Order

## Folder

Run everything from: `dan-guide/lesson14-Webscraping-and-dashboard`

## Setup (once)

- Activate your venv: `source .venv/Scripts/activate`
- Install deps: `python -m pip install --upgrade pip` then `python -m pip install selenium pandas streamlit altair`
- Make sure Google Chrome is installed.

## Run Order

### p1.py - scrape to CSV
- **Run:** `py p1.py`
- **Creates:** `batting_avg_league_leaders.csv`

### clean.py - clean CSV
- **Run:** `py clean.py`
- **Creates:** `batting_avg_cleaned.csv`, `removed.txt`

### p2.py - load into SQLite
- **Run:** `py p2.py`
- **Creates or overwrites:** `batting_avg.db` (table: `batting_avg_leaders`)

### p3.py - optional CLI queries
- **Run:** `py p3.py`
- Use the menu to query by year, AVG threshold, or team.

### p4.py - optional Streamlit dashboard
- **Run:** `python -m streamlit run p4.py`
- Opens a local app to explore charts and filters.

## When to re-run

- If site data or scraper changes: run `p1` → `clean` → `p2`
- If only cleaning changes: run `clean` → `p2`
- For queries or UI only: run `p3` or `p4`

## Quick tips

- If `streamlit` is not found, use `python -m streamlit run p4.py`
- If the DB is not found, confirm you ran `p2.py` in the same folder
- Check you are in the right directory with `pwd` and list files with `ls`