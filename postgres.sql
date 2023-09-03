CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);

CREATE TABLE account_roles (
  user_id INT NOT NULL,
  role_id INT NOT NULL,
  grant_date TIMESTAMP,
  PRIMARY KEY (user_id, role_id),
  FOREIGN KEY (role_id)
      REFERENCES roles (role_id),
  FOREIGN KEY (user_id)
      REFERENCES accounts (user_id)
);


CREATE TABLE book (
	book_id serial PRIMARY KEY,
	title VARCHAR ( 50 ) UNIQUE NOT NULL,
	author VARCHAR ( 50 ),	
	created_on TIMESTAMP NOT null default now()     
);

select * from book;

insert into book (title, author) values ('Test Book', 'Test Author');


-- SQL Structured Query Language

drop table car;

CREATE TABLE car (	
	car_id serial primary key,
	make VARCHAR ( 50 ),
	model VARCHAR ( 50 ) unique		
);

create trigger on insert 
	go to the UNINSURABLE_CARS table and check if this car exists

delete from car;

-- Car Insurance 
insert into car (make, model) values ('Ford', 'F-250') returning car_id;



insert into car (make, model) values ('Honda', 'Civic');
insert into car (make, model) values ('Toyota', 'Corolla');
insert into car (make, model) values ('Toyota', 'Land Cruiser');

insert into car (make, model) values 
('Honda', 'Accord'),
('Honda', 'Civic'),
('Toyota', 'Corolla'),
('Toyota', 'Land Cruiser') 
;

insert 
-- CRUD - create, read, update , delete

select * from car order by car_id;

select car_id, make, model from car;

-- UNINSURABLE_CARS
CREATE TABLE UNINSURABLE_CARS (	
	car_id serial primary key,
	make VARCHAR ( 50 ),
	model VARCHAR ( 50 ) unique	
);

update car 
	set model = 'BLAH BLAH'
	where car_id = 27;


insert into UNINSURABLE_CARS(make, model) values ('Volkswagen', 'Jetta');

select * from UNINSURABLE_CARS order by car_id;

select * from car order by car_id;
-- Result Set



update car set model = 'CRV' where car_id = 4;

delete from car where car_id = 17;



create transaction
	update checking_account set amount = amount - 200 where user_id = 232232;		
	update saving_account set amount = amount + 200 where user_id = 232232;
commit;

drop table customer;
create table customer (
	customer_id serial primary key,
	name varchar(50) not null,
	phone varchar(20)
);

insert into customer (name, phone) values 
	('John Doe', '416-555-1212'),
	('Jane Doe', '416-555-1213')
;

select * from customer;

create table customer_order (
	customer_order_id serial primary key,
	description varchar(100) not null,
	special_instructions varchar(250),
	customer_id int
);

insert into customer_order (description, special_instructions, customer_id)
values ('Thinkpad P1', 'Handle with care', 25);

select * from customer_order;

drop table customer_order2;

create table customer_order2 (
	customer_order_id serial primary key,
	description varchar(100) not null,
	special_instructions varchar(250),
	customer_id int,
	foreign key(customer_id) references customer(customer_id)
);

insert into customer_order2 (description, special_instructions, customer_id)
values ('Thinkpad P1', 'Handle with care', 25);

select * from customer_order2;

-- 1 to 1 cardinality

CREATE TABLE person (	
	person_id serial primary key,
	person_name VARCHAR ( 50 )	
);

CREATE TABLE passport (	
	passport_id serial primary key,
	passport_number int not null,
	person_id int
);

-- drop table person;
-- drop table passport;

select * from person;
select * from passport;

insert into person (person_name) values ('John Doe');
insert into passport (passport_number, person_id) values (10001, 1);

select person_name, passport_number
	from person
	join passport on passport.person_id = person.person_id;




drop table book;

CREATE TABLE book (
	book_id serial PRIMARY KEY,
	title VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT null default now(),
	author_id int,
	FOREIGN KEY(author_id) REFERENCES author(author_id)
);

CREATE TABLE author (
	author_id serial PRIMARY KEY,
	author VARCHAR ( 50 ),	
	author_country varchar(50),
	created_on TIMESTAMP NOT null default now()     
);

CREATE TABLE project_developer (
	project_id int,
	developer_id int,
	FOREIGN KEY(project_id) REFERENCES project(project_id),
	FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
);

drop table book;
delete from book;

select * from author;
select * from book;

select book_id, title, a.author_id, author, author_country
from book b, author a
where b.author_id = a.author_id;

insert into author (author, author_country) values 
	('Author 1', 'Latvia'),
	('Author 2', 'Lithuvania'),
	('Author 3', 'Estonia');

insert into book (title, author_id) values 
	('Book 3', 1);

-- We want out TABLES to be focused, have data about one and only one entity

-- Normalization

-- 1st normal form
-- 2nd normal form
 




