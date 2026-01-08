DROP TABLE IF EXISTS staging.hr_attrition_clean;

CREATE TABLE staging.hr_attrition_clean AS
SELECT
    "EmployeeNumber"::INT            AS employee_number,
    "Age"::INT                       AS age,
    "Gender"                         AS gender,
    "Department"                    AS department,
    "JobRole"                       AS job_role,
    "MonthlyIncome"::INT             AS monthly_income,
    "Attrition"                     AS attrition
FROM raw.hr_attrition_raw;

