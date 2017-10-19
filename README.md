# logs-analysis-project
This project uses the PostgreSQL Python wrapper Psycopg to query a server log for a mock newspaper site in order to return information, in plain text, addressing the following prompts:

1. **What are the three most popular articles of all time?**
2. **Who are the most popular article authors of all time?**
3. **On which days did more than 1% of all requests lead to errors?**

The `news` database contains the following three tables: 
* `articles` 
* `authors`
* `log`  

# Setup
The following SQL Views must be defined in the `news` database before execution:
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
