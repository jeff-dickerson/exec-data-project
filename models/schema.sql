-- Schema for AI Impact Tracking System

-- Industries table to track different sectors
CREATE TABLE Industries (
    industry_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Initiatives table to track AI/LLM projects
CREATE TABLE Initiatives (
    initiative_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50) CHECK (status IN ('planned', 'in_progress', 'completed', 'on_hold')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Metrics table to define measurable outcomes
CREATE TABLE Metrics (
    metric_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    unit VARCHAR(50),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table linking Initiatives to Industries
CREATE TABLE InitiativeIndustries (
    initiative_id INTEGER REFERENCES Initiatives(initiative_id),
    industry_id INTEGER REFERENCES Industries(industry_id),
    PRIMARY KEY (initiative_id, industry_id)
);

-- Junction table linking Initiatives to Metrics
CREATE TABLE InitiativeMetrics (
    initiative_id INTEGER REFERENCES Initiatives(initiative_id),
    metric_id INTEGER REFERENCES Metrics(metric_id),
    target_value NUMERIC,
    target_date DATE,
    PRIMARY KEY (initiative_id, metric_id)
);

-- Table for actual performance outcomes
CREATE TABLE PerformanceOutcomes (
    outcome_id SERIAL PRIMARY KEY,
    initiative_id INTEGER REFERENCES Initiatives(initiative_id),
    metric_id INTEGER REFERENCES Metrics(metric_id),
    actual_value NUMERIC,
    measurement_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial data for Oil & Gas industry
INSERT INTO Industries (name, description) 
VALUES ('Oil & Gas', 'Oil and Gas industry including upstream, midstream, and downstream operations');

-- Insert initial initiative for Crude Oil Production Monitoring
INSERT INTO Initiatives (name, description, status) 
VALUES (
    'Crude Oil Production Monitoring',
    'AI-powered monitoring and prediction of crude oil production trends',
    'in_progress'
);

-- Insert initial metric for Crude Oil Production Volume
INSERT INTO Metrics (name, description, unit, category) 
VALUES (
    'Crude Oil Production Volume',
    'Monthly crude oil production volume in thousands of barrels per day',
    'k bbl/day',
    'production'
);

-- Link initiative to industry
INSERT INTO InitiativeIndustries (initiative_id, industry_id)
VALUES (1, 1);

-- Link initiative to metric
INSERT INTO InitiativeMetrics (initiative_id, metric_id)
VALUES (1, 1); 