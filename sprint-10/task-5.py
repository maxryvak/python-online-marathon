update customers set city="Paris", grade=300 where id=3003;
select name, city, grade from customers where city in ("London", "Paris") order by id 
