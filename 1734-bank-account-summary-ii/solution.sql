# Write your MySQL query statement below
SELECT p.name, SUM(k.amount) AS balance
FROM Users p
JOIN Transactions k ON p.account = k.account
GROUP BY p.account, p.name
HAVING SUM(k.amount) > 10000;
