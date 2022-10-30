select customers.name, customers.city, sum(orders.amount) as totalSum from customers inner join orders on orders.customer_id=customers.id
where orders.amount between 100 and 3500 group by customers.name order by customers.city
