import sqlalchemy

engin = sqlalchemy.create_engine('postgresql://ulitka:afybz011187@localhost:5432/lesson2')
connection = engin.connect()

connection.execute('''INSERT INTO genre
VALUES(1, 'Rock'),
(2, 'Pop'),
(3, 'Classic'),
(4, 'Rap'),
(5, 'Disco');''')

connection.execute('''INSERT INTO singer
VALUES(1, 'hands_up'),
(2, 'zivert'),
(3, 'splin'),
(4, 'eminem'),
(5, 'boomboks'),
(6, 'noize_mc'),
(7, 'monetochka'),
(8, 'Bach');''')

connection.execute('''INSERT INTO album
VALUES(1, 'dont be afraid', 2001),
(2, 'Vinyl #1', 2019),
(3, 'New people', 2003),
(4, 'The Eminem Show', 2002),
(5, 'all inclusive', 2017),
(6, 'exit to the city', 2021),
(7, 'Arts and Crafts', 2020),
(8, 'Bach: A New Recital', 2022);''')

connection.execute('''INSERT INTO collection
VALUES(1, 'collection1', 2019),
(2, 'collection2', 2016),
(3, 'collection3', 2015),
(4, 'collection4', 2009),
(5, 'collection5', 2006),
(6, 'collection6', 2021),
(7, 'collection7', 2020),
(8, 'collection8', 2022);''')

connection.execute('''INSERT INTO track
VALUES(1, 1, 'Im already 18', 210),
(2, 2, 'life', 185),
(3, 3, 'handball', 195),
(4, 3, 'New people', 186),
(5, 4, 'Superman', 210),
(6, 5, 'no cold', 220),
(7, 5, 'I am yours', 175),
(8, 6, 'voyager', 240),
(9, 6, '26.04', 200),
(10, 6, 'vudu', 190),
(11, 7, 'Chit', 175),
(12, 7, 'Syringe', 185),
(13, 7, 'radiograph', 205),
(14, 7, 'Ice', 215),
(15, 8, 'Fantasia and Fugue', 300);''')

connection.execute('''INSERT INTO album_singer
VALUES(1, 2),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(2, 4),
(3, 5),
(4, 6),
(5, 2),
(6, 4),
(7, 8),
(8, 8);''')

connection.execute('''INSERT INTO collection_track
VALUES(1, 2),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 4),
(9, 5),
(10, 6),
(11, 2),
(12, 4),
(13, 8),
(14, 2),
(15, 3),
(4, 3),
(5, 4),
(6, 3),
(7, 5),
(8, 6),
(9, 4),
(10, 2),
(11, 3),
(12, 8),
(13, 2),
(14, 8);''')

connection.execute('''INSERT INTO genre_singer
VALUES(1, 2),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 5),
(7, 2),
(2, 4),
(3, 1),
(4, 3),
(5, 4),
(6, 3),
(7, 5),
(8, 2);''')
