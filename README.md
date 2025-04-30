# AI Impact Tracking - Oil & Gas Industry Pilot

## Project Overview
This project aims to create executive-driven AI insights for measurable business impact across industries, starting with the Oil & Gas sector as a lighthouse pilot. It establishes a canonical dataset structure for tracking AI/LLM/AI Agents initiatives and their outcomes.

## Project Structure
```
.
├── data/
│   ├── raw/          # Raw data files from EIA API
│   └── processed/    # Processed and transformed data
├── ingestion/        # Data ingestion scripts
├── models/          # Database schema and DDL
├── notebooks/       # Jupyter notebooks for analysis
├── dashboards/      # Visualization and reporting
└── docs/           # Documentation and data dictionary
```

## Setup Instructions

### Environment Setup
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### API Key Setup
1. Obtain an API key from the [EIA website](https://www.eia.gov/opendata/)
2. Set the API key as an environment variable:
   - Windows: `set EIA_API_KEY=your_key_here`
   - Unix/MacOS: `export EIA_API_KEY=your_key_here`

### Running the Project
1. Data Ingestion:
   ```bash
   python ingestion/fetch_crude_production.py
   ```

2. Database Setup:
   - Follow instructions in `models/schema.sql`

3. Analysis:
   - Open Jupyter notebooks in the `notebooks/` directory
   - View dashboards in the `dashboards/` directory

## Contributing
Please follow the standard Git workflow:
1. Create a feature branch
2. Make changes
3. Submit a pull request

## License
[Add appropriate license] 