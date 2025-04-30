import pandas as pd
import plotly.express as px
import os

def create_and_save_trend_chart():
    """
    Reads the processed crude production data and generates an interactive
    Plotly line chart, saving it as an HTML file.
    """
    # --- Configuration ---
    # Assumes script is run from the project root
    csv_path = os.path.join("data", "raw", "crude_production_24mo.csv")
    output_html_path = os.path.join("dashboards", "crude_production_trend.html")

    # --- Load Data ---
    print(f"Loading data from: {csv_path}")
    try:
        df = pd.read_csv(csv_path, parse_dates=['Month'])
        print(f"Successfully loaded {len(df)} rows.")
    except FileNotFoundError:
        print(f"Error: Input CSV not found at {csv_path}.")
        print("Please ensure the ingestion script (ingestion/fetch_crude_production.py) has been run successfully.")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # --- Create Plot ---
    print("Generating Plotly chart...")
    try:
        fig = px.line(
            df,
            x='Month',
            y='Crude_Oil_Production_MBBL',
            title='U.S. Monthly Crude Oil Field Production Trend (Last ~24 Months)',
            labels={'Month': 'Date', 'Crude_Oil_Production_MBBL': 'Production (Thousand Barrels)'},
            markers=True # Add markers to data points
        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Production (Thousand Barrels)",
            hovermode="x unified" # Improve hover experience
        )
    except Exception as e:
        print(f"Error creating Plotly chart: {e}")
        return

    # --- Save Chart as HTML ---
    print(f"Saving chart to: {output_html_path}")
    try:
        # Ensure the output directory exists (it should, but double-check)
        os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
        fig.write_html(output_html_path)
        print("Chart saved successfully.")
    except Exception as e:
        print(f"Error saving HTML file: {e}")

if __name__ == "__main__":
    create_and_save_trend_chart() 