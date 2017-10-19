# logs-analysis-project

# SQL Views
The source code for this project requires the following views:
```sql
CREATE VIEW requests_per_day AS
SELECT DATE(time) AS day, COUNT(*) AS requests
FROM log
GROUP BY day;

CREATE VIEW errors_per_day AS
SELECT DATE(time) AS day, COUNT(*) AS errors
FROM log
WHERE status LIKE '404%'
GROUP BY day;
```
