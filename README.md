# Open_Meteo_Weather_Project 

A small data ingestion project built while learning how to work with APIs as part of my transition into data engineering. This script fetches live weather forecast data for Nairobi from the [Open-Meteo API](https://open-meteo.com/), structures it with pandas, and categorizes daily temperatures.

## About This Project

This was built as a hands-on exercise in API ingestion — the first step in most real-world data pipelines. Rather than working with a static file, this project pulls live data directly from a public API, parses the JSON response, and transforms it into a usable structure.

## What This Script Does

- Sends a GET request to the Open-Meteo API for Nairobi's 7-day weather forecast
- Parses the JSON response into a Python dictionary
- Converts the nested `daily` data into a pandas DataFrame
- Categorizes each day's maximum temperature as cold, mild, or hot
- Exports the result to a clean CSV file

## Example Output

| time       | temperature_2m_max | temperature_2m_min | category |
|------------|--------------------|--------------------|----------|
| 2026-06-18 | 23.7               | 14.0               | mild     |
| 2026-06-19 | 24.6               | 14.8               | mild     |
| 2026-06-20 | 22.2               | 14.2               | mild     |

## Tools Used

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Files

- `weather.py` — main script: fetch, parse, categorize, and export
- `nairobi_weather.csv` — output file with categorized forecast data

## How to Run

```bash
pip install requests pandas
python weather.py
```

## What I Learned

This project was my first hands-on work with APIs after building a pandas-based data cleaning project. Key takeaways:

- How a GET request and JSON response actually work, beyond the theory — sending a request, receiving structured data back, and parsing it
- Navigating nested dictionaries to extract exactly the data needed
- Converting a dictionary of lists directly into a pandas DataFrame
- Using `.apply()` to run custom logic across every row of a column without writing an explicit loop
- Debugging a "stale file" issue where saved code didn't match what was actually running — a reminder to always verify the file on disk matches what's in the editor before assuming the logic is wrong

## Part of a Larger Journey

This is one of several practice projects building toward a larger goal: a data pipeline examining livestock disease surveillance data across Africa, built in tribute to my father's work as a veterinary epidemiologist who contributed to the global eradication of rinderpest. API ingestion specifically will be a core part of that pipeline, pulling data from international animal health organizations.

---

*Built as part of a self-directed transition from web development to data engineering, June 2026.*
