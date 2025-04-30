# Executive AI Analysis: Foundational Dataset Structure

A Foundational Dataset Structure for Tracking AI/LLM Initiatives Across Industries

## Table of Contents

- [Project Overview](#project-overview)
- [Executive Summary](#executive-summary)
- [Data Structure](#data-structure)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Recommendations](#recommendations)
- [Getting Started (Setup & Usage)](#getting-started-setup--usage)
  - [Project File Structure](#project-file-structure)
  - [Setup Instructions](#setup-instructions)
  - [Running the Project Steps](#running-the-project-steps)

---

## Project Overview

The integration of AI and LLMs is rapidly transforming industries, offering unprecedented opportunities for innovation, efficiency gains, and enhanced customer experiences. As organizations increasingly invest in these technologies, the ability to systematically track their implementation and quantify their impact becomes paramount. However, measuring the true business value derived from AI/LLM initiatives presents several challenges. These include the diverse nature of AI applications across different sectors, the lack of standardized metrics for evaluation, and the difficulty in establishing clear causal links between AI adoption and business outcomes. To address these challenges, this report outlines a foundational dataset structure intended to provide a consistent and comprehensive framework for tracking and analyzing AI/LLM initiatives. This structure aims to enable organizations to move beyond anecdotal evidence and gain a data-driven understanding of their AI/LLM investments, facilitating informed strategic decisions and maximizing the potential return on these transformative technologies.

This project implements this foundational structure, starting with a pilot focused on the Oil & Gas industry using publicly available data.

## Executive Summary

The proliferation of Artificial Intelligence (AI) and Large Language Models (LLMs) across diverse sectors has created an imperative for organizations to systematically track their adoption and measure their impact. This report proposes a foundational dataset structure designed to facilitate this tracking, enabling strategic decision-making grounded in empirical evidence. The structure encompasses key dimensions, including detailed information about AI/LLM initiatives, the specific industry segments they affect with examples of notable companies, a comprehensive suite of performance metrics encompassing cost-related Key Performance Indicators (KPIs), and the crucial relationships that interconnect these elements. By leveraging publicly available data sources and adapting existing data models, organizations can implement this framework to gain a holistic understanding of their AI/LLM landscape, optimize investments, and drive innovation. The proposed dataset structure includes interconnected tables for initiatives, industries, metrics, and performance outcomes, allowing for detailed analysis of the adoption, impact, and ROI of AI/LLM technologies across various business functions.

## Data Structure

The core of this project is a proposed canonical data structure designed to track AI/LLM initiatives and their measurable impact. The draft schema is defined in `models/schema.sql` and aims to capture the key entities involved:

*   **`Initiatives`**: Details about specific AI/LLM projects or programs being undertaken (e.g., name, description, status, owner, timeframe).
*   **`Industries`**: Information about the industry sectors relevant to the initiatives.
*   **`Metrics`**: Definitions of the specific key performance indicators (KPIs) used to measure the impact of initiatives (e.g., cost savings, production volume, adoption rate, efficiency gain).
*   **`PerformanceOutcomes`**: Time-series data capturing the measured values of specific `Metrics` for given `Initiatives` over time.
*   **Junction Tables**: (e.g., `InitiativeIndustries`) To manage many-to-many relationships.

A detailed breakdown of each table and column is available in the **[Data Dictionary](./docs/data_dictionary.md)**.

This structure provides a flexible yet standardized way to link strategic initiatives to tangible performance outcomes, allowing for analysis across different projects, metrics, and industries.

## Data Sources

This initial pilot project uses publicly available data from the U.S. Energy Information Administration (EIA) API.

*   **Source:** EIA API v2
*   **Dataset:** U.S. Field Production of Crude Oil, Monthly
*   **Series ID:** `PET.MCRFPUS2.M`

The data is fetched using the script `ingestion/fetch_crude_production.py`.

Future iterations plan to incorporate additional public datasets (e.g., pricing, rig counts, petrochemicals) and potentially allow for integration with internal company data sources.

## Exploratory Data Analysis (EDA)

A preliminary EDA for the pilot dataset (Crude Oil Production) is available in the Jupyter Notebook: `notebooks/eda_crude_production.ipynb`.

This notebook includes:
*   Loading and inspecting the raw data.
*   A time-series plot of monthly production.
*   Calculation of the percentage change over the period.

An example visualization (interactive HTML chart) can also be generated by running `dashboards/plot_crude_trend.py`.

## Recommendations

Based on the initial pilot setup, the following next steps are recommended:

1.  **Database Implementation:** Set up a target database (e.g., Snowflake, PostgreSQL) and implement the DDL from `models/schema.sql`. Refine the `ingestion/load_crude_outcomes.py` script to connect and load data into the database.
2.  **Expand Data Sources:** Integrate additional relevant datasets (e.g., WTI prices, Baker Hughes rig counts) by creating new ingestion scripts and potentially new metric definitions.
3.  **Refine Metrics & Categories:** Review and expand the `Metrics` table and `metric_category` enum based on specific business needs and the data available for different initiatives.
4.  **Enhance Dashboards:** Develop more comprehensive dashboards (using Plotly Dash, PowerBI, Streamlit, etc.) connecting directly to the database to visualize relationships between initiatives, metrics, and outcomes.
5.  **CI/CD Pipeline:** Enhance the GitHub Actions workflow to include automated database schema migration, data loading tests (if feasible), and potentially scheduled data ingestion runs.

---

## Getting Started (Setup & Usage)

### Project File Structure

```
/
├── .github/workflows/ci.yml  # CI workflow
├── .gitignore
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── venv/                     # Python virtual environment (Git ignored)
├── data/
│   ├── raw/                  # Raw data as fetched from sources
│   │   └── crude_production_24mo.csv
│   └── processed/            # Processed or cleaned data (if any)
├── dashboards/
│   ├── plot_crude_trend.py   # Script to generate Plotly HTML chart
│   └── crude_production_trend.html # Generated HTML chart (Git ignored?)
├── docs/
│   └── data_dictionary.md    # Description of database tables/columns
├── ingestion/
│   ├── fetch_crude_production.py # Script to fetch EIA data
│   └── load_crude_outcomes.py    # Placeholder script for DB loading logic
├── models/
│   └── schema.sql            # Draft database schema (DDL)
└── notebooks/
    └── eda_crude_production.ipynb # Exploratory Data Analysis notebook
```

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/jeff-dickerson/exec-data-project.git
    cd exec-data-project
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows (PowerShell)
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # Note: requirements.txt includes pandas, requests, plotly, flake8.
    # Install Jupyter separately if needed to run the notebook:
    # pip install jupyterlab
    ```

4.  **Set EIA API Key:**
    This project requires an API key from the U.S. Energy Information Administration (EIA). You can obtain one [here](https://www.eia.gov/opendata/register.php).

    The `ingestion/fetch_crude_production.py` script expects the key as an environment variable named `EIA_API_KEY`.

    **Set it for your current terminal session *after* activating the virtual environment:**
    -   **Linux/macOS:** `export EIA_API_KEY='YOUR_API_KEY'`
    -   **Windows (PowerShell):** `$env:EIA_API_KEY='YOUR_API_KEY'`

    *(Replace `YOUR_API_KEY` with your actual key.)*

### Running the Project Steps

1.  **Fetch Raw Data:**
    Ensure your `EIA_API_KEY` is set, then run:
    ```bash
    python ingestion/fetch_crude_production.py
    ```
    Creates/updates `data/raw/crude_production_24mo.csv`.

2.  **Database Loading (Placeholder):**
    The script `ingestion/load_crude_outcomes.py` outlines the logic for loading the CSV into a database (does not perform actual DB operations).
    ```bash
    python ingestion/load_crude_outcomes.py
    ```

3.  **Exploratory Data Analysis:**
    Launch Jupyter Lab/Notebook and open `notebooks/eda_crude_production.ipynb`. Run cells.
    ```bash
    jupyter lab
    ```

4.  **Generate Dashboard Chart:**
    Run the dashboard script:
    ```bash
    python dashboards/plot_crude_trend.py
    ```
    Creates/updates `dashboards/crude_production_trend.html`. Open this file in your browser.

## Database Schema

See `models/schema.sql` for the draft DDL for tables like `Initiatives`, `Metrics`, and `PerformanceOutcomes`.

## Data Dictionary

See `docs/data_dictionary.md` (when created) for details on table columns and types. 