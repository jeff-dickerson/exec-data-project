-- Initial Schema Draft for AI Impact Tracking
-- Target Database: Snowflake (or adjust as needed)

-- Enum type for metric categories (adjust values as needed)
CREATE TYPE metric_category AS ENUM (
    'VOLUME', 
    'COST', 
    'TIME', 
    'QUALITY', 
    'EFFICIENCY', 
    'ADOPTION', 
    'SATISFACTION', 
    'OTHER'
);

-- Enum type for initiative status
CREATE TYPE initiative_status AS ENUM (
    'PLANNING',
    'ACTIVE',
    'COMPLETED',
    'ON_HOLD',
    'CANCELLED'
);

-- Table for Industries
CREATE TABLE Industries (
    IndustryID SERIAL PRIMARY KEY,
    IndustryName VARCHAR(255) UNIQUE NOT NULL,
    Description TEXT
);

-- Table for AI/LLM Initiatives
CREATE TABLE Initiatives (
    InitiativeID SERIAL PRIMARY KEY,
    InitiativeName VARCHAR(255) NOT NULL,
    Description TEXT,
    StartDate DATE,
    EndDate DATE,
    Status initiative_status DEFAULT 'PLANNING',
    Owner VARCHAR(100) -- Or link to a Users table
);

-- Table for Metrics being tracked
CREATE TABLE Metrics (
    MetricID SERIAL PRIMARY KEY,
    MetricName VARCHAR(255) NOT NULL,
    Description TEXT,
    UnitOfMeasure VARCHAR(50),
    Category metric_category,
    IsHigherBetter BOOLEAN -- Indicates if a higher value is generally better
);

-- Table for Performance Outcomes (Time Series Data)
-- This table links to both an Initiative and a Metric
CREATE TABLE PerformanceOutcomes (
    OutcomeID SERIAL PRIMARY KEY,
    InitiativeID INT NOT NULL,
    MetricID INT NOT NULL,
    OutcomeDate DATE NOT NULL, -- Or TIMESTAMP for higher precision
    OutcomeValue DECIMAL(18, 4), -- Adjust precision as needed
    Notes TEXT,
    DataSource VARCHAR(255),
    LoadTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (InitiativeID) REFERENCES Initiatives(InitiativeID),
    FOREIGN KEY (MetricID) REFERENCES Metrics(MetricID),
    UNIQUE (InitiativeID, MetricID, OutcomeDate) -- Ensure uniqueness per initiative/metric/date
);

-- Junction table linking Initiatives to Industries
CREATE TABLE InitiativeIndustries (
    InitiativeID INT NOT NULL,
    IndustryID INT NOT NULL,
    PRIMARY KEY (InitiativeID, IndustryID),
    FOREIGN KEY (InitiativeID) REFERENCES Initiatives(InitiativeID),
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID)
);

-- Optional: Junction table linking Initiatives to specific Metrics directly (if needed beyond Outcomes)
-- CREATE TABLE InitiativeMetrics (
--     InitiativeID INT NOT NULL,
--     MetricID INT NOT NULL,
--     PRIMARY KEY (InitiativeID, MetricID),
--     FOREIGN KEY (InitiativeID) REFERENCES Initiatives(InitiativeID),
--     FOREIGN KEY (MetricID) REFERENCES Metrics(MetricID)
-- );

-- Sample Data (Illustrative)
-- INSERT INTO Industries (IndustryName, Description) VALUES ('Oil & Gas', 'Exploration, production, refining, and distribution of oil and natural gas.');
-- INSERT INTO Initiatives (InitiativeName, Description, Status, Owner) VALUES ('Crude Oil Production Monitoring', 'Pilot project using EIA data for monitoring US crude production trends', 'ACTIVE', 'Project Lead');
-- INSERT INTO Metrics (MetricName, UnitOfMeasure, Category, IsHigherBetter) VALUES ('Crude Oil Production Volume', 'Thousand Barrels', 'VOLUME', True);
-- Note: PerformanceOutcomes data loaded via script.
-- INSERT INTO InitiativeIndustries (InitiativeID, IndustryID) VALUES (1, 1); 