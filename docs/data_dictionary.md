# Data Dictionary

This document describes the tables defined in `models/schema.sql`.

## Enums

### `metric_category`

Specifies the type or domain of a metric.

*   `VOLUME`: Quantity or amount.
*   `COST`: Monetary value.
*   `TIME`: Duration or frequency.
*   `QUALITY`: Level of quality or defects.
*   `EFFICIENCY`: Ratio of output to input.
*   `ADOPTION`: Rate or level of usage.
*   `SATISFACTION`: User or customer satisfaction level.
*   `OTHER`: Any other category.

### `initiative_status`

Tracks the current lifecycle state of an initiative.

*   `PLANNING`: Initiative is being planned.
*   `ACTIVE`: Initiative is currently in progress.
*   `COMPLETED`: Initiative has finished.
*   `ON_HOLD`: Initiative progress is temporarily paused.
*   `CANCELLED`: Initiative has been stopped before completion.

---

## Tables

### `Industries`

Stores information about different industries relevant to the initiatives.

| Column         | Type         | Constraints                   | Description                                      |
| -------------- | ------------ | ----------------------------- | ------------------------------------------------ |
| `IndustryID`   | `SERIAL`     | `PRIMARY KEY`                 | Unique identifier for the industry.              |
| `IndustryName` | `VARCHAR(255)` | `UNIQUE NOT NULL`           | Name of the industry (e.g., "Oil & Gas").        |
| `Description`  | `TEXT`       |                               | Optional description of the industry.            |

### `Initiatives`

Tracks specific AI/LLM/Agent initiatives.

| Column           | Type                | Constraints        | Description                                                         |
| ---------------- | ------------------- | ------------------ | ------------------------------------------------------------------- |
| `InitiativeID`   | `SERIAL`            | `PRIMARY KEY`      | Unique identifier for the initiative.                             |
| `InitiativeName` | `VARCHAR(255)`      | `NOT NULL`         | Name of the initiative.                                             |
| `Description`    | `TEXT`              |                    | Detailed description of the initiative.                             |
| `StartDate`      | `DATE`              |                    | Date the initiative started or is planned to start.               |
| `EndDate`        | `DATE`              |                    | Date the initiative ended or is planned to end.                 |
| `Status`         | `initiative_status` | `DEFAULT PLANNING` | Current status of the initiative (uses `initiative_status` enum). |
| `Owner`          | `VARCHAR(100)`      |                    | Person or team responsible for the initiative.                      |

### `Metrics`

Defines the specific metrics being tracked across initiatives.

| Column          | Type              | Constraints   | Description                                                               |
| --------------- | ----------------- | ------------- | ------------------------------------------------------------------------- |
| `MetricID`      | `SERIAL`          | `PRIMARY KEY` | Unique identifier for the metric.                                         |
| `MetricName`    | `VARCHAR(255)`    | `NOT NULL`    | Name of the metric (e.g., "Crude Oil Production Volume").                 |
| `Description`   | `TEXT`            |               | Detailed description of the metric.                                       |
| `UnitOfMeasure` | `VARCHAR(50)`     |               | Unit for the metric's value (e.g., "Thousand Barrels", "USD", "Hours"). |
| `Category`      | `metric_category` |               | Category of the metric (uses `metric_category` enum).                     |
| `IsHigherBetter`| `BOOLEAN`         |               | Indicates if a higher value is generally considered better for this metric. |

### `PerformanceOutcomes`

Stores the time-series data points for specific metrics related to specific initiatives.

| Column          | Type           | Constraints                       | Description                                                                        |
| --------------- | -------------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| `OutcomeID`     | `SERIAL`       | `PRIMARY KEY`                     | Unique identifier for the outcome record.                                          |
| `InitiativeID`  | `INT`          | `NOT NULL`, `FOREIGN KEY`         | Links to the `Initiatives` table.                                                  |
| `MetricID`      | `INT`          | `NOT NULL`, `FOREIGN KEY`         | Links to the `Metrics` table.                                                      |
| `OutcomeDate`   | `DATE`         | `NOT NULL`                        | The date (or timestamp) associated with this specific outcome value.               |
| `OutcomeValue`  | `DECIMAL(18, 4)`|                                   | The numeric value of the metric on the `OutcomeDate`. Adjust precision as needed. |
| `Notes`         | `TEXT`         |                                   | Optional notes or context about this specific data point.                          |
| `DataSource`    | `VARCHAR(255)` |                                   | Source of this data point (e.g., script name, API endpoint, manual entry).       |
| `LoadTimestamp` | `TIMESTAMP`    | `DEFAULT CURRENT_TIMESTAMP`       | Timestamp when the record was loaded into the table.                             |
| *Unique Index*  |                | `(InitiativeID, MetricID, OutcomeDate)` | Ensures only one value per metric per initiative per date.                       |

### `InitiativeIndustries`

Junction table linking initiatives to one or more relevant industries.

| Column         | Type  | Constraints               | Description                               |
| -------------- | ----- | ------------------------- | ----------------------------------------- |
| `InitiativeID` | `INT` | `NOT NULL`, `PRIMARY KEY` | Links to the `Initiatives` table.         |
| `IndustryID`   | `INT` | `NOT NULL`, `PRIMARY KEY` | Links to the `Industries` table.          |

</rewritten_file> 