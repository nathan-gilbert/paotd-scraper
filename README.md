# Prog Album Release Date Scraper

[![Pylint](https://github.com/nathan-gilbert/paotd-scraper/actions/workflows/pylint.yml/badge.svg)](https://github.com/nathan-gilbert/paotd-scraper/actions/workflows/pylint.yml)

Scrapes Wikipedia for Prog Artists, Albums and Release Dates

### Running

- `python3 -m venv venv`
- `source venv/bin/activate.fish`
- `python run_wikipedia_scraper.py` -- scrapes wikipedia for albums from the 
  `artist_list.txt`
- `python run_apple_scraper.py` -- runs the apple music scraper and creates 
  a csv file of all the albums from the listed artists.

### TODO