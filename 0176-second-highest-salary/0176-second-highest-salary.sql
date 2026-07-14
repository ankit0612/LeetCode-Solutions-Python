/* Write your T-SQL query statement below */
-- select E1.salary as SecondHighestSalary 
--     from Employee E1
--     join Employee E2 on 
--     E1.salary = E2.salary where
--     E1.salary > E2.salary

select max(salary) as SecondHighestSalary
    from Employee 
    where salary < (select max(salary) from Employee);
