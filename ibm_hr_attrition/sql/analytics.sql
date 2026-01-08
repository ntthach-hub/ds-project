CREATE SCHEMA IF NOT EXISTS analytics;

DROP TABLE IF EXISTS analytics.attrition_summary;

CREATE TABLE analytics.attrition_summary AS
SELECT
    department,
    attrition,
    COUNT(*) AS employee_count,
    AVG(monthly_income) AS avg_income
FROM staging.hr_attrition_clean
GROUP BY department, attrition;
