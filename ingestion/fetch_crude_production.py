#!/usr/bin/env python3
"""
fetch_crude_production.py

Fetches the last 24 months of U.S. field crude oil production
from the EIA Open Data API and saves it to a CSV file.
"""

import os
import requests
import pandas as pd
from datetime import datetime
# import pprint # No longer needed

def fetch_and_process_crude_production():
    """
    Fetches U.S. Field Production of Crude Oil from the EIA API, processes it,
    and saves the last 24 months to a CSV file.

    Requires the EIA_API_KEY environment variable to be set.
    """
    # --- DEBUG: Print all environment variables ---
    # print("--- All Environment Variables ---")
    # pprint.pprint(dict(os.environ))
    # print("----------------------------------")
    # --- END DEBUG ---

    # 1. Get API Key from environment variable
    # Remember to set the EIA_API_KEY environment variable before running!
    api_key = os.getenv("EIA_API_KEY")
    # api_key = "e9hHQUJPf0AMi9i9Q0xQ4IXRaSZLEDVeWuA4qU95" # !!! TEMPORARY HARDCODED KEY - REMOVE LATER !!! # Removed
    if not api_key:
        # Provide a more user-friendly error if the key isn't set
        raise ValueError("EIA_API_KEY environment variable not set. Please set it before running the script.")

    # 2. Define API endpoint and parameters
    # Series ID: U.S. Field Production of Crude Oil, Monthly
    series_id = "PET.MCRFPUS2.M"
    # api_url = f"https://api.eia.gov/series/?api_key={api_key}&series_id={series_id}" # Old V1 style URL
    api_url = f"https://api.eia.gov/v2/seriesid/{series_id}?api_key={api_key}" # New V2 style URL for V1 Series ID

    print(f"Fetching data for series: {series_id}...")
    # print(f"DEBUG: Using API Key: {api_key[:5]}...{api_key[-5:]}") # Removed
    try:
        # 3. Make HTTP GET request
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        # print("DEBUG: API request successful.") # Removed
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return

    # 4. Parse JSON response
    try:
        # print("DEBUG: Attempting to parse JSON...") # Removed
        data = response.json()
        # print("DEBUG: JSON parsed successfully.") # Removed
        # print("DEBUG: Raw JSON data:", data) # Optional: Uncomment to see full JSON

        # Adjusted structure for V2 API response
        if 'response' not in data or 'data' not in data['response']:
            print("Error: 'response' or 'data' key not found in V2 API response structure.")
            print("Response content:", data)
            return

        series_data = data['response']['data']
        # print("DEBUG: Extracted series_data.") # Removed
    except (ValueError, KeyError, IndexError) as e:
        print(f"Error parsing JSON response: {e}")
        # print("Response content:", response.text) # Print raw text if JSON fails
        return
    except Exception as e:
        print(f"An unexpected error occurred during JSON parsing: {e}")
        # print("Response content:", response.text)
        return

    # 5. Convert to pandas DataFrame
    # print("DEBUG: Attempting to create DataFrame...") # Removed
    # Adjusted columns and date format for V2
    df = pd.DataFrame(series_data, columns=['period', 'value'])
    # print("DEBUG: DataFrame created.") # Removed

    # 6. Data Type Conversion
    # print("DEBUG: Attempting data type conversion...") # Removed
    # Convert 'period' (YYYY-MM string) to datetime objects
    df['date'] = pd.to_datetime(df['period'], format='%Y-%m')

    # Convert 'value' to numeric, coercing errors to NaN
    df['production'] = pd.to_numeric(df['value'], errors='coerce')

    # Remove rows with NaN in production (e.g., if conversion failed)
    df.dropna(subset=['production'], inplace=True)

    # Ensure DataFrame is sorted by date in descending order to easily get the last months
    df.sort_values(by='date', ascending=False, inplace=True)

    # 7. Filter for the last 24 months
    df_filtered = df.head(24)

    # Sort back to ascending order for the final CSV - Avoid SettingWithCopyWarning
    df_filtered = df_filtered.sort_values(by='date', ascending=True)
    # df_filtered.sort_values(by='date', ascending=True, inplace=True) # Original line causing warning

    # Select and rename columns for clarity
    # print("DEBUG: Attempting to rename columns...") # Removed
    df_final = df_filtered[['date', 'production']].copy() # Use .copy() here too for safety
    df_final.rename(columns={'date': 'Month', 'production': 'Crude_Oil_Production_MBBL'}, inplace=True) # MBBL = Thousand Barrels
    # print("DEBUG: Columns renamed.") # Removed

    # 8. Define output path and write to CSV (Using absolute path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    output_dir = os.path.join(project_root, "data", "raw")
    os.makedirs(output_dir, exist_ok=True) # Ensure directory exists
    output_path = os.path.join(output_dir, "crude_production_24mo.csv")
    # print(f"DEBUG: Attempting to save CSV to absolute path: {output_path}") # Removed

    try:
        df_final.to_csv(output_path, index=False)
        print(f"Successfully saved last 24 months of data to: {output_path}")
    except IOError as e:
        print(f"Error writing CSV file: {e}")

if __name__ == "__main__":
    fetch_and_process_crude_production()
