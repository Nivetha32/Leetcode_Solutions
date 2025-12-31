# Write your MySQL query statement below
select concat(year(trans_date), '-', lpad(month(trans_date),2,'0')) as month , country , count(*) as trans_count, sum(state ='approved') as approved_count, sum(amount) as trans_total_amount, sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END) as approved_total_amount
from Transactions
group by year(trans_date),month(trans_date), country;
