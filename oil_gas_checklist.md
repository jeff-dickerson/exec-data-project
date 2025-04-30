- [ ] **Repo & Environment Setup**  
  - [ ] Initialize a new GitHub repository (e.g. `ai-impact-oil-gas`)  
  - [ ] Add a `README.md` with project overview and folder structure  
  - [ ] Create `.gitignore` (ignore `venv/`, `.env`, `*.pyc`, `__pycache__/`)  

- [ ] **Virtual Environment & Dependencies**  
  - [ ] Create a Python 3.8+ virtual environment (`python3 -m venv venv`)  
  - [ ] Activate the virtualenv (`source venv/bin/activate` or `venv\Scripts\activate`)  
  - [ ] Install required packages (`pip install pandas requests`)  
  - [ ] Freeze dependencies to `requirements.txt`  

- [ ] **API Key Management**  
  - [ ] Add instructions in `README.md` for setting `EIA_API_KEY` as an environment variable  
  - [ ] Ensure `.env` or local config is ignored by Git  

- [ ] **Data Ingestion Script**  
  - [ ] Under `/ingestion/`, create `fetch_crude_production.py` with:  
    - Reading `EIA_API_KEY` from `os.getenv`  
    - HTTP GET to `https://api.eia.gov/series/` with `series_id=PET.MCRFPUS2.M`  
    - JSON parsing into a pandas DataFrame  
    - Date conversion (`YYYYMM` → `datetime`)  
    - Filtering last 24 months of data  
    - Writing output to `/data/raw/crude_production_24mo.csv`  
  - [ ] Write docstring and inline comments explaining each step  

- [ ] **Folder Structure & GitHub Org**  
  - [ ] Create `/data/` with subfolders `/raw/`, `/processed/`  
  - [ ] Create `/notebooks/` for exploratory work  
  - [ ] Create `/models/` for DDL or schema definitions  
  - [ ] Create `/dashboards/` for PowerBI/Plotly exports  

- [ ] **Schema Definition**  
  - [ ] Under `/models/`, draft `schema.sql` or Snowflake DDL for:  
    - Table `Initiatives`  
    - Table `Metrics`  
    - Table `PerformanceOutcomes`  
    - Junction tables (`InitiativeMetrics`, `InitiativeIndustries`, etc.)  
  - [ ] Include data types, primary/foreign keys, enums for metric categories  

- [ ] **Sample Data Load**  
  - [ ] Run `fetch_crude_production.py` to generate `crude_production_24mo.csv`  
  - [ ] Manually inspect the CSV to confirm 24 rows and correct fields  

- [ ] **Database Ingestion**  
  - [ ] Write a short script or SQL loader to ingest CSV into `PerformanceOutcomes` table  
  - [ ] Create or upsert a record in `Initiatives` for “Crude Oil Production Monitoring”  
  - [ ] Create or upsert a record in `Metrics` for “Crude Oil Production Volume”  
  - [ ] Link the loaded outcomes to the above initiative & metric via `InitiativeMetrics`  

- [ ] **Exploratory Data Analysis**  
  - [ ] Open `/notebooks/eda_crude_production.ipynb`  
  - [ ] Plot time series of monthly production using pandas/Plotly  
  - [ ] Compute simple % change from first to last month  

- [ ] **Dashboard Prototype**  
  - [ ] Under `/dashboards/`, create a basic Plotly script (`plot_crude_trend.py`) that:  
    - Reads processed data from the database or CSV  
    - Generates an interactive line chart of production vs. time  
    - Saves as `crude_production_trend.html`  
  - [ ] Alternatively, import the CSV into PowerBI and build a single-page executive dashboard  

- [ ] **Documentation & Data Dictionary**  
  - [ ] Update `README.md` with:  
    - How to set up environment  
    - How to run the ingestion script  
    - How to load data into the database  
    - How to launch EDA notebook and dashboard  
  - [ ] Create `/docs/data_dictionary.md` detailing each table’s columns and types  

- [ ] **CI / Automation**  
  - [ ] Add a GitHub Actions workflow (`.github/workflows/ci.yml`) to:  
    - Lint Python files (e.g. `flake8`)  
    - Run `fetch_crude_production.py --dry-run` (check for script errors)  
  - [ ] Configure scheduled dispatch (e.g. monthly) if ongoing data refresh is needed  

- [ ] **Review & Merge**  
  - [ ] Open a Pull Request with all changes  
  - [ ] Conduct code review, verify scripts run end-to-end  
  - [ ] Merge into `main` branch once approved  

- [ ] **Next Steps Planning**  
  - [ ] Plan extending to petrochemicals dataset or additional KPIs (prices, rigs)  
  - [ ] Define second pilot for dashboard interactivity and user filters  
