#!/usr/bin python3
import psycopg2 as psy

# Create a new Connection to database
db = psy.connect(dbname="news")

# Create cursor
c = db.cursor()

# 1. Top three articles.
c.execute("""
SELECT title, COUNT(*)
FROM articles, log
WHERE slug = SUBSTRING(path, 10)
GROUP BY path, title
ORDER BY COUNT(*) DESC
LIMIT 3;
""")

print()

print("Top Three Most Popular Articles:")

for row in c.fetchall():
    print('\t"{}" - {} views'.format(row[0].title(),
                                     row[1]))

print()

# 2. Most popular authors.
c.execute("""
SELECT name, COUNT(*)
FROM articles, log, authors
WHERE slug = SUBSTRING(path, 10) AND authors.id = author
GROUP BY name
ORDER BY COUNT(*) DESC
""")

print("Most Popular Authors:")

for row in c.fetchall():
    print('\t{} - {} views'.format(row[0], row[1]))

print()

# 3. Days where more than 1% of requests led to errors.
c.execute("""
SELECT err.day AS date,
       CAST(errors AS float) / requests * 100 AS percent
FROM errors_per_day AS err,
     requests_per_day AS req
WHERE err.day = req.day
      AND CAST(errors AS float) / requests > 0.01;
""")

print("Days where more than 1% of Requests led to Errors:")

for row in c.fetchall():
    print("\t{} - {}% errors".format(row[0].strftime("%B %d, %Y"),
                                     round(row[1], 1)))

print()
# Close Connection
db.close()
