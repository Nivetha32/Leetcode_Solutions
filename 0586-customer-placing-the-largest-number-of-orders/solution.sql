# Write your MySQL query statement below
With t1 as 

(

  Select customer_number, 

  Rank() over(order by count(customer_number) desc) as rk

  from orders

  group by customer_number

) 

Select t1.customer_number

from t1

where t1.rk=1
