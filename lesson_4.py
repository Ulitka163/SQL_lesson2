import sqlalchemy

engin = sqlalchemy.create_engine('postgresql://ulitka:afybz011187@localhost:5432/lesson2')
connection = engin.connect()

print(connection.execute('''SELECT genre_id, COUNT(singer_id) FROM genre_singer
GROUP BY genre_id
ORDER BY genre_id;
''').fetchall())

print(connection.execute('''SELECT album, COUNT(track) FROM track
JOIN album ON track.album_id = album.id
WHERE album.year >= 2019 and album.year <= 2020
GROUP BY album;
''').fetchall())

print(connection.execute('''SELECT album_id, AVG(duration) FROM track
GROUP BY album_id
ORDER BY album_id;
''').fetchall())

print(connection.execute('''SELECT DISTINCT singer.name FROM singer
JOIN album_singer ON singer.id = album_singer.singer_id
WHERE singer_id NOT IN (SELECT singer_id FROM album_singer
JOIN album ON album_singer.album_id = album.id
WHERE year = 2020)
ORDER BY singer.name;
''').fetchall())

print(connection.execute('''SELECT DISTINCT collection.name FROM collection
JOIN collection_track ON collection.id = collection_track.collection_id
JOIN track ON collection_track.track_id = track.id
JOIN album ON track.album_id = album.id
JOIN album_singer ON album.id = album_singer.album_id
JOIN singer ON album_singer.singer_id = singer.id
WHERE singer.name LIKE 'monetochka';
''').fetchall())

print(connection.execute('''SELECT DISTINCT album.name FROM album
JOIN album_singer ON album.id = album_singer.album_id
JOIN singer ON album_singer.singer_id = singer.id
WHERE singer_id IN (
SELECT singer_id FROM genre_singer
GROUP BY genre_singer.singer_id
HAVING COUNT(genre_singer.genre_id) > 1);
''').fetchall())

print(connection.execute('''SELECT track.name FROM track
LEFT JOIN collection_track c ON track.id = c.track_id
WHERE c.track_id IS NULL;
''').fetchall())

print(connection.execute('''SELECT s.name FROM singer s
JOIN album_singer a ON s.id = a.singer_id
JOIN album ON a.album_id = album.id
JOIN track ON album.id = track.album_id
WHERE track.duration = (SELECT MIN(duration) FROM track);
''').fetchall())

print(connection.execute('''SELECT a.name, COUNT(track.id) FROM album a
JOIN track ON a.id = track.album_id
GROUP BY a.name
HAVING COUNT(track.id) = (SELECT count(id) FROM track
GROUP BY album_id
ORDER BY count(id)
LIMIT 1);
''').fetchall())