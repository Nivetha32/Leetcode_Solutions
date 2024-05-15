# Write your MySQL query statement below
select Email
from (Select Email,count(Email)
from person 
      group by Email
      having count(Email)>1)a;
