CREATE DATABASE IF NOT EXISTS book;
USE book;

CREATE TABLE IF NOT EXISTS publisher
(
	ID int not null,
    name varchar(255) not null,
    constraint PK_publisher primary key (ID)
);

CREATE TABLE IF NOT EXISTS author
(
	ID int not null,
    lastname varchar(50),
    middlename varchar(50),
    firstname varchar(50),
    constraint PK_author primary key (ID)
);

CREATE TABLE IF NOT EXISTS book 
(
	ID int not null,
	title varchar(255) not null,
    pages int,
    rating decimal(4,2),
    ISBN varchar(13),
    published_date date,
    publisher_ID int,
    constraint PK_book primary key (ID),
    constraint FK_book foreign key (publisher_ID) references publisher(ID)
);
    
CREATE TABLE IF NOT EXISTS book_author
(
	book_ID int not null,
    author_ID int not null,
    constraint PK_book_author primary key (book_ID, author_ID),
    constraint FK_book_author_book foreign key (book_ID) references book(ID) on delete cascade,
    constraint FK_book_author_author foreign key (author_ID) references author(ID) on delete cascade
);

CREATE TABLE IF NOT EXISTS genre
(
	ID int not null,
    name varchar(50),
    parent_ID int,
    constraint PK_genre primary key (ID),
    constraint FK_genre foreign key (parent_ID) references genre(ID)
);

CREATE TABLE IF NOT EXISTS book_genre
(
	book_ID int not null,
    genre_ID int not null,
    constraint PK_book_genre primary key(book_ID,genre_ID),
    constraint FK_book_genre_book foreign key(book_ID) references book(ID) on delete cascade,
    constraint FK_book_genre_genre foreign key(genre_ID) references genre(ID) on delete cascade
)