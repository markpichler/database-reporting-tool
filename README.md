# logs-analysis-project
This project uses the PostgreSQL Python wrapper Psycopg to query the server log of a mock newspaper site in order to return information, in plain text, addressing the following prompts:

1. **What are the three most popular articles of all time?**
2. **Who are the most popular article authors of all time?**
3. **On which days did more than 1% of all requests lead to errors?**

Refer to the [Output file](./output.txt) to see the program's returned information.

# Database Summary
The `news` database contains the following three tables: 
* `articles` stores information on the news articles. 
* `authors` stores information about the authors.
* `log` stores information on server requests.    

# Setup
This application uses the Psycopg 2 Python package.  To set up the environment, simply type the following in the terminal:
```
pip install -r requirements.txt
```
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
To execute this application, run the following Python module from the terminal:
```shell
python3 logs_reporting_tool.py
```
