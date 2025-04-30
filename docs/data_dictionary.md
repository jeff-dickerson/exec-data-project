# Data Dictionary

## Tables Overview

### Industries
Tracks different industry sectors where AI initiatives are implemented.

| Column | Type | Description |
|--------|------|-------------|
| industry_id | SERIAL | Primary key |
| name | VARCHAR(100) | Industry name (unique) |
| description | TEXT | Detailed description of the industry |
| created_at | TIMESTAMP | Record creation timestamp |

### Initiatives
Tracks AI/LLM projects and their status.

| Column | Type | Description |
|--------|------|-------------|
| initiative_id | SERIAL | Primary key |
| name | VARCHAR(200) | Initiative name |
| description | TEXT | Detailed description of the initiative |
| start_date | DATE | Project start date |
| end_date | DATE | Project end date |
| status | VARCHAR(50) | Current status (planned/in_progress/completed/on_hold) |
| created_at | TIMESTAMP | Record creation timestamp |

### Metrics
Defines measurable outcomes for initiatives.

| Column | Type | Description |
|--------|------|-------------|
| metric_id | SERIAL | Primary key |
| name | VARCHAR(200) | Metric name |
| description | TEXT | Detailed description of the metric |
| unit | VARCHAR(50) | Unit of measurement |
| category | VARCHAR(100) | Metric category |
| created_at | TIMESTAMP | Record creation timestamp |

### InitiativeIndustries
Junction table linking initiatives to industries.

| Column | Type | Description |
|--------|------|-------------|
| initiative_id | INTEGER | Foreign key to Initiatives |
| industry_id | INTEGER | Foreign key to Industries |

### InitiativeMetrics
Junction table linking initiatives to metrics with targets.

| Column | Type | Description |
|--------|------|-------------|
| initiative_id | INTEGER | Foreign key to Initiatives |
| metric_id | INTEGER | Foreign key to Metrics |
| target_value | NUMERIC | Target value for the metric |
| target_date | DATE | Target achievement date |

### PerformanceOutcomes
Records actual performance measurements.

| Column | Type | Description |
|--------|------|-------------|
| outcome_id | SERIAL | Primary key |
| initiative_id | INTEGER | Foreign key to Initiatives |
| metric_id | INTEGER | Foreign key to Metrics |
| actual_value | NUMERIC | Measured value |
| measurement_date | DATE | Date of measurement |
| created_at | TIMESTAMP | Record creation timestamp |

## Relationships

- One Initiative can be associated with multiple Industries (through InitiativeIndustries)
- One Industry can have multiple Initiatives (through InitiativeIndustries)
- One Initiative can track multiple Metrics (through InitiativeMetrics)
- One Metric can be tracked by multiple Initiatives (through InitiativeMetrics)
- One Initiative can have multiple PerformanceOutcomes
- One Metric can have multiple PerformanceOutcomes 