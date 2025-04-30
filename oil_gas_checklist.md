- [x] **Repo & Environment Setup**  
  - [x] Initialize a new GitHub repository (e.g. `ai-impact-oil-gas`)  
  - [x] Add a `README.md` with project overview and folder structure  
  - [x] Create `.gitignore` (ignore `venv/`, `.env`, `*.pyc`, `__pycache__/`)  

- [x] **Virtual Environment & Dependencies**  
  - [x] Create a Python 3.8+ virtual environment (`python3 -m venv venv`)  
  - [x] Activate the virtualenv (`source venv/bin/activate` or `venv\Scripts\activate`)  
  - [x] Install required packages (`pip install pandas requests`)  
  - [x] Freeze dependencies to `requirements.txt`  

- [x] **API Key Management**  
  - [x] Add instructions in `README.md` for setting `EIA_API_KEY` as an environment variable  
  - [x] Ensure `.env` or local config is ignored by Git  

- [x] **Data Ingestion Script**  
  - [x] Under `/ingestion/`, create `fetch_crude_production.py` with:  
    - Reading `EIA_API_KEY` from `os.getenv`  
    - HTTP GET to `https://api.eia.gov/series/` with `series_id=PET.MCRFPUS2.M`  
    - JSON parsing into a pandas DataFrame  
    - Date conversion (`YYYYMM` → `datetime`)  
    - Filtering last 24 months of data  
    - Writing output to `/data/raw/crude_production_24mo.csv`  
  - [x] Write docstring and inline comments explaining each step  

- [x] **Folder Structure & GitHub Org**  
  - [x] Create `/data/` with subfolders `/raw/`, `/processed/`  
  - [x] Create `/notebooks/` for exploratory work  
  - [x] Create `/models/` for DDL or schema definitions  
  - [x] Create `/dashboards/` for PowerBI/Plotly exports  
  - [x] Create `/docs/` folder  

- [x] **Schema Definition**  
  - [x] Under `/models/`, draft `schema.sql` or Snowflake DDL for:  
    - Table `Initiatives`  
    - Table `Metrics`  
    - Table `PerformanceOutcomes`  
    - Junction tables (`InitiativeMetrics`, `InitiativeIndustries`, etc.)  
  - [ ] Include data types, primary/foreign keys, enums for metric categories  

- [x] **Sample Data Load**  
  - [x] Run `fetch_crude_production.py` to generate `crude_production_24mo.csv`  
  - [x] Manually inspect the CSV to confirm 24 rows and correct fields  

- [ ] **Database Ingestion**  
  - [ ] Write a short script or SQL loader to ingest CSV into `PerformanceOutcomes` table  
  - [ ] Create or upsert a record in `Initiatives` for "Crude Oil Production Monitoring"  
  - [ ] Create or upsert a record in `Metrics` for "Crude Oil Production Volume"  
  - [ ] Link the loaded outcomes to the above initiative & metric via `InitiativeMetrics`  

- [x] **Exploratory Data Analysis**  
  - [x] Open `/notebooks/eda_crude_production.ipynb`  
  - [ ] Plot time series of monthly production using pandas/Plotly  
  - [ ] Compute simple % change from first to last month  

- [x] **Dashboard Prototype**  
  - [x] Under `/dashboards/`, create a basic Plotly script (`plot_crude_trend.py`) that:  
    - Reads processed data from the database or CSV  
    - Generates an interactive line chart of production vs. time  
    - Saves as `crude_production_trend.html`  
  - [-] Alternatively, import the CSV into PowerBI and build a single-page executive dashboard  

- [x] **Documentation & Data Dictionary**  
  - [x] Update `README.md` with:  
    - How to set up environment  
    - How to run the ingestion script  
    - How to load data into the database (placeholder script info)
    - How to launch EDA notebook and dashboard  
  - [x] Create `/docs/data_dictionary.md` detailing each table's columns and types  

- [x] **CI / Automation**  
  - [x] Add a GitHub Actions workflow (`.github/workflows/ci.yml`) to:  
    - Lint Python files (e.g. `flake8`)  
    - Run `fetch_crude_production.py` (check for script errors, uses dummy API key)  
  - [ ] Configure scheduled dispatch (e.g. monthly) if ongoing data refresh is needed  

- [ ] **Review & Merge**  
  - [ ] Open a Pull Request with all changes  
  - [ ] Conduct code review, verify scripts run end-to-end  
  - [ ] Merge into `main` branch once approved  

- [ ] **Next Steps Planning**  
  - [ ] Plan extending to petrochemicals dataset or additional KPIs (prices, rigs)  
  - [ ] Define second pilot for dashboard interactivity and user filters  




Productionized Next Steps

- [ ] **Stakeholder Validation & Requirement Refinement**  
  - [ ] Schedule a walkthrough demo of the pilot dashboard with executive sponsors and key data stewards  
  - [ ] Collect feedback on KPI definitions, industry labels, timeframes, and visualization needs  
  - [ ] Update data dictionary and schema to reflect any newly requested metrics or nomenclature  

- [ ] **Extend KPI Coverage**  
  - [ ] Identify and document additional EIA series (e.g. WTI/Brent prices, Henry Hub gas prices, active rig counts)  
  - [ ] Write new ingestion code under `/ingestion/` for each series, following the `fetch_crude_production.py` pattern  
  - [ ] Add corresponding entries in `Metrics` (e.g. “WTI Spot Price”, unit “USD/bbl”)  
  - [ ] Map pre-/post- dates and load into `PerformanceOutcomes`  

- [ ] **Onboard Petrochemicals Subset**  
  - [ ] Research public petrochemical production APIs or CSV sources (e.g. UN Comtrade, IHS Markit samples)  
  - [ ] Write ETL connector script to fetch & normalize ethylene, propylene production data  
  - [ ] Add “Industry” record for “Petrochemicals” and link initiatives via `InitiativeIndustries`  
  - [ ] Define new Metrics (e.g. “Ethylene Production Volume”, unit “kt/year”) and load sample data  

- [ ] **Implement Data Quality & Governance Checks**  
  - [ ] Define validation rules (e.g. no negative values, no missing dates in a series)  
  - [ ] Integrate data-quality tests into ingestion scripts (raise errors or log warnings)  
  - [ ] Build a lightweight data catalog (e.g. JSON or Markdown pages) to describe table fields, sources, refresh cadence  
  - [ ] Commit catalog to `/docs/data_catalog.md` and keep in sync with schema changes  

- [ ] **Automate & Schedule Pipelines**  
  - [ ] Containerize ingestion scripts with a `Dockerfile` (base Python image, mount `/ingestion/` and `/data/`)  
  - [ ] Create CI/CD pipeline in GitHub Actions or Airflow:  
    - [ ] Step 1: Pull latest code  
    - [ ] Step 2: Build Docker image  
    - [ ] Step 3: Run ingestion container (reads `EIA_API_KEY` from secrets)  
    - [ ] Step 4: Validate outputs and push CSVs or load directly into database  
  - [ ] Configure scheduled runs (e.g. monthly cron) and failure alerts (Slack/email)  

- [ ] **Production Database & Access Controls**  
  - [ ] Deploy schema DDL to production data warehouse (Snowflake/Redshift/BigQuery)  
  - [ ] Create database roles and grants:  
    - [ ] `data_engineer` (full DDL and write permissions)  
    - [ ] `analyst` (read-only access to all tables)  
    - [ ] `executive` (read-only access to dashboards only)  
  - [ ] Rotate and store API keys and credentials in a secrets manager (AWS Secrets Manager or Vault)  

- [ ] **Dashboard Hardening & UX Enhancements**  
  - [ ] Add interactive filters to the Plotly/PowerBI dashboard:  
    - [ ] Industry selector  
    - [ ] Time-range slider  
    - [ ] Metric category dropdown  
  - [ ] Embed narrative annotations or tooltips explaining key inflection points  
  - [ ] Publish dashboard to a shareable endpoint (PowerBI Service workspace or Plotly Dash Enterprise)  

- [ ] **Performance & Cost Optimization**  
  - [ ] Implement clustering/partitioning on time-series tables for faster queries (e.g. partition by month/year)  
  - [ ] Monitor query performance and adjust warehouse compute sizing as needed  
  - [ ] Track API usage against EIA limits; throttle or cache results to control costs  

- [ ] **Documentation & Training**  
  - [ ] Finalize `README.md` with:  
    - [ ] Environment setup  
    - [ ] How to run and schedule ingestion  
    - [ ] How to load or query production tables  
    - [ ] How to access and interpret the dashboard  
  - [ ] Update `/docs/data_dictionary.md` to reflect all new tables and columns  
  - [ ] Record a 10–15 minute “how-to” demo video for end users and ops team  
  - [ ] Host a live training session or office hours for analysts and stakeholders  

- [ ] **Phase 2 Roadmap & Pilots**  
  - [ ] Draft a 6–12 month roadmap for onboarding Manufacturing, Retail, Healthcare datasets  
  - [ ] Define success metrics and KPI targets for each new industry pilot  
  - [ ] Allocate resources and schedule sprints for subsequent phases  


