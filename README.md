## API Sales ETL Pipeline

**JSONPlaceholder API → 1000 Sales Records → Executive Analytics**

## Business Problem
Built end-to-end pipeline analyzing sales rep performance across 4 regions using live API data from JSONPlaceholder.

## Tech Stack
- Python (Pandas/Requests) 
- Excel (Pivot tables/Vlookups)
- SQLite (SQL analytics)
- Postman (API validation)

## Key Results
Top Sales Rep: Clementina DuBuque - ₹7.6M revenue (West region)
Total Orders Processed: 1000+
Regions Analyzed: North, South, East, West
Data Quality: 100% cleaned and deduplicated

## Pipeline Flow
LIVE API (JSONPlaceholder) → Data Extraction → Cleaning/Transformation → Excel Pivots → SQL Analytics → Stakeholder Reports

## Run Locally
pip install pandas requests openpyxl
python etl_pipeline.py

## Skills Demonstrated
- API integration and platform-to-platform data flows
- Processing large datasets (1000+ records daily)
- Excel pivot tables, Vlookups, deduplication
- SQL GROUP BY analytics and business reporting
- Postman API testing and validation
- End-to-end ETL pipeline development

## Business Impact
Identified top-performing sales representative generating ₹7.6M revenue across West region. Created executive-ready pivot tables and SQL analytics for stakeholder review.

## Quick Demo
Run `python etl_pipeline.py` generates all analytics files in 10 seconds. Postman collection validates API endpoints used in pipeline.
