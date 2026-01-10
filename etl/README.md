# ETL Examples - Data Engineering

This directory contains examples of Data Engineering work, specifically ETL (Extract, Transform, Load) pipelines and data processing scripts.

## Contents

1. **`simple_etl.py`** - Basic ETL pipeline example
2. **`data_validation.py`** - Data quality validation script
3. **`api_data_collector.py`** - Example of collecting data from APIs
4. **`database_loader.py`** - Example of loading data into a database

## What is ETL?

**ETL (Extract, Transform, Load)** is the core process in data engineering:

- **Extract**: Gather data from various sources (APIs, databases, files)
- **Transform**: Clean, validate, and restructure the data
- **Load**: Store the processed data in a destination (database, data warehouse)

## Running the Examples

Each script can be run independently:

```bash
# Simple ETL pipeline
python simple_etl.py

# Data validation
python data_validation.py

# API data collection
python api_data_collector.py

# Database loading (requires database setup)
python database_loader.py
```

## Data Engineering vs Data Science

**Data Engineer's Role:**
- Build and maintain these ETL pipelines
- Ensure data quality and reliability
- Automate data collection and processing
- Optimize data storage and retrieval

**Data Scientist's Role:**
- Use the clean data produced by DE
- Perform exploratory data analysis
- Build machine learning models
- Generate insights and predictions

## Learning Resources

- [Apache Airflow](https://airflow.apache.org/) - Workflow orchestration
- [Luigi](https://github.com/spotify/luigi) - Pipeline framework
- [Great Expectations](https://greatexpectations.io/) - Data validation
- [dbt](https://www.getdbt.com/) - Data transformation tool
