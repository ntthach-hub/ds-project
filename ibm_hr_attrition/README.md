# IBM HR Atrrition Data Pipeline 

## Overview
This project demonstrates an end to end data engineering pipeline using Python and Postgresql on the IBM HR Attrition dataset.

## Architecture
CSV -> Raw -> Staging -> Analytics

## Tech Stack
- Python
- PostgreSQL
- SQLAlchemy

## Pipeline Flow
1. Ingest raw CSV data into PostgreSQL (raw schema)
2. Clean and transform data into staging layer
3. Aggregate data for analytics use cases
4. Orchestrate pipeline execution with python

## How to Run

``bash
python main.py  