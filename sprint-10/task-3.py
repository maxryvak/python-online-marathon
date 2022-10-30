select orders.order_num, orders.amount, customers.name from customers inner join orders on orders.customer_id=customers.id
where orders.amount between 500 and 2000 order by orders.order_num
