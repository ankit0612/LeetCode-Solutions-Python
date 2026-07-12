# Write your MySQL query statement below
SELECT W1.id
    FROM Weather as W1
    Join Weather as W2 on
    W1.temperature > W2.temperature AND
    DATEDIFF(W1.recordDate, W2.recordDate) = 1;