# Write your MySQL query statement below
select id from (select id, recordDate,temperature,LAG(temperature) OVER (ORDER BY recordDate) AS p_temp ,   LAG(recordDate) OVER (ORDER BY recordDate) AS p_date from Weather) t
where temperature > p_temp
and DATEDIFF(recordDate, p_date) = 1;





