USE olist_db;
CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    day_of_week VARCHAR(20),
    is_weekend BOOLEAN
);

INSERT INTO dim_date (date_key, year, quarter, month, month_name, day_of_week, is_weekend)
WITH RECURSIVE date_generator AS (
    SELECT CAST('2016-09-01' AS DATE) AS date_val
    UNION ALL
    SELECT DATE_ADD(date_val, INTERVAL 1 DAY)
    FROM date_generator
    WHERE date_val < '2018-10-31'
)
SELECT
    date_val AS date_key,
    YEAR(date_val) AS year,
    QUARTER(date_val) AS quarter,
    MONTH(date_val) AS month,
    MONTHNAME(date_val) AS month_name,
    DAYNAME(date_val) AS day_of_week,
    CASE WHEN DAYOFWEEK(date_val) IN (1, 7) THEN TRUE ELSE FALSE END AS is_weekend
FROM date_generator;