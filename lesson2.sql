create table if not exists genre (
	id serial primary key,
	name varchar(40) not null unique
);

create table if not exists singer (
	id serial primary key,
	name varchar(40) not null unique
);

create table if not exists genre_singer (
	singer_id integer references singer(id),
	genre_id integer references genre(id),
	constraint genre_singer_key primary key (singer_id, genre_id) 
);

create table if not exists album (
	id serial primary key,
	name varchar(40) not null unique,
	year integer not null	
);

create table if not exists album_singer (
	album_id integer references album(id),
	singer_id integer references singer(id),
	constraint album_singer_key primary key (album_id, singer_id)
);

create table if not exists collection (
	id serial primary key,
	name varchar(40) not null unique,
	year integer not null
);

create table if not exists track (
	id serial primary key,
	album_id integer references album(id),
	name varchar(40) not null unique,
	duration integer not null
);

create table if not exists collection_track (
	track_id integer references track(id),
	collection_id integer references collection(id),
	constraint collection_track_key primary key (track_id, collection_id)
);