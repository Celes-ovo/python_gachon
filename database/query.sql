create table product(
    pid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER);


insert into product(name, price) values('Iphone 13 pro', 1300000);
insert into product(name, price) values('Galaxy S22', 1100000);
insert into product(name, price) values('LG V50', 950000);

select * from product;

select * from product where pid=2;

delete from product;

delete from product where pid=10;