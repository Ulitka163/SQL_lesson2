import sqlalchemy

engin = sqlalchemy.create_engine('postgresql://ulitka:afybz011187@localhost:5432/lesson2')
connection = engin.connect()

print(connection.execute('''SELECT name, year FROM album
WHERE year = 2018;
''').fetchall())

print(connection.execute('''SELECT name, duration FROM track
ORDER BY duration DESC
LIMIT 1;
''').fetchall())

print(connection.execute('''SELECT name FROM track
WHERE duration < 210;
''').fetchall())

print(connection.execute('''SELECT name FROM collection
WHERE year > 2018 AND year <= 2020;
''').fetchall())
#
print(connection.execute('''SELECT name FROM singer
WHERE name NOT LIKE '%% %%';
''').fetchall())

print(connection.execute('''SELECT name FROM track
WHERE name iLIKE '%%my%%';
''').fetchall())