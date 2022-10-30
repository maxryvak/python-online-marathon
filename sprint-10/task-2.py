insert into customers (id, name, city, grade, salesperson_id) values (3006, "Stefan Huk", "Kyiv", 500, 5007);
select * from customers where city in ("London", "Kyiv") order by id
