#!/usr/bin/env python3
"""
fetch_crude_production.py

Fetches the last 24 months of U.S. field crude oil production
from the EIA Open Data API and saves it to a CSV file.
"""

import os
import sys
import requests
import pandas as pd
from datetime import datetime

# 1. Read your API key from the environment
API_KEY = os.getenv("EIA_API_KEY")
if not API_KEY:
    sys.exit("ERROR: Please set your EIA_API_KEY environment variable before running this script.")

# 2. Define the series ID and endpoint
SERIES_ID = "PET.MCRFPUS2.M"  # U.S. field crude oil production (k bbl/day)
EIA_URL   = "https://api.eia.gov/series/"

# 3. Fetch the data
resp = requests.get(EIA_URL, params={"api_key": API_KEY, "series_id": SERIES_ID})
resp.raise_for_status()  # stop if anything went wrong

data = resp.json().get("series", [])[0].get("data", [])
if not data:
    sys.exit("ERROR: No data returned from EIA API.")

# 4. Load into a DataFrame
df = pd.DataFrame(data, columns=["period", "production"])
df["period"] = pd.to_datetime(df["period"], format="%Y%m")

# 5. Filter to the most recent 24 months
latest = df["period"].max()
cutoff = latest - pd.DateOffset(months=24)
df = df[(df["period"] > cutoff) & (df["period"] <= latest)].reset_index(drop=True)

# 6. Output
output_file = "crude_production_24mo.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} rows to {output_file}")
