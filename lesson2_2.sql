create table if not exists worker (
	id serial primary key,
	name varchar(40) not null unique
);

create table if not exists department (
	id serial primary key,
	name varchar(40) not null unique,
	worker_id integer references worker(id)
);

create table if not exists worker_department (
	worker_id integer references worker(id),
	department_id integer references department(id),
	constraint worker_department_key primary key (worker_id, department_id)
);