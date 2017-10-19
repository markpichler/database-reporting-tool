# logs-analysis-project

# Setup
The following SQL Views must be defined in the "news" database before execution:
```sql
-- A two column table showing the total number of requests per day.
CREATE VIEW requests_per_day AS
SELECT DATE(time) AS day, COUNT(*) AS requests
FROM log
GROUP BY day;

-- A two column table showing the number of erroneous requests per day.
CREATE VIEW errors_per_day AS
SELECT DATE(time) AS day, COUNT(*) AS errors
FROM log
WHERE status LIKE '404%'
GROUP BY day;
```
# Execution
Simply type the following in the terminal to run this application:
```shell
python3 logs_reporting_tool.py
```
