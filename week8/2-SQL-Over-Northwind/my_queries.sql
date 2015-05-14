-- 1. List all employees with their first name, last name and title.
SELECT FirstName AS first_name, LastName AS last_name, Title AS title
FROM employees;

-- 2. List all employees from Seattle.
SELECT FirstName || " "  ||  LastName AS name, City 
FROM employees 
WHERE City = 'Seattle';

-- 3. List all employees from London.
SELECT FirstName || " "  ||  LastName AS name, City 
FROM employees 
WHERE City = 'London';

-- 4. List all employees that work in the Sales department.
SELECT FirstName || " "  ||  LastName AS name, Title 
FROM employees 
WHERE Title LIKE  "%Sales%";

-- 5. List all females employees that work in the Sales department.
SELECT FirstName || " "  ||  LastName AS name, Title, TitleOfCourtesy 
FROM employees WHERE Title LIKE  "%Sales%"
AND TitleOfCourtesy IN ("Ms.", "Mrs.");

-- 6. List the 5 oldest employees.
SELECT FirstName || " "  ||  LastName AS name, BirthDate
FROM employees
ORDER BY BirthDate ASC
LIMIT 5;

-- 7. List the first 5 hires of the company.
SELECT FirstName || " "  ||  LastName AS name, HireDate
FROM employees
ORDER BY HireDate ASC
LIMIT 5;

-- 8. List the employee who reports to no one (the boss)
SELECT  FirstName || " "  ||  LastName AS name, EmployeeID, ReportsTo
FROM employees
WHERE ReportsTo IS NULL;

-- 9. List all employes by their first and last name, and the first and last name of the employees that they report to.
SELECT e1.FirstName || " "  ||  e1.LastName AS employee_name,
		e2.FirstName || " "  ||  e2.LastName AS manager_name
FROM employees AS e1
INNER JOIN employees AS e2
ON e1.ReportsTo = e2.EmployeeID;

-- 10. Count all female employees.
SELECT COUNT(EmployeeID) AS female_count
FROM employees
WHERE TitleOfCourtesy IN ("Ms.", "Mrs.");

-- 11. Count all male employees.
SELECT COUNT(EmployeeID) AS male_count
FROM employees
WHERE TitleOfCourtesy IN ("Mr.", "Dr.");

-- 12. Count how many employees are there from the different cities. For example, there are 4 employees from London.
SELECT City, COUNT(EmployeeID) AS different_cities_count
FROM employees
GROUP BY City;

-- 13. List all OrderIDs and the employees (by first and last name) that have created them.
SELECT orders.OrderID, employees.FirstName || " " || employees.LastName AS name
FROM orders 
JOIN employees
ON orders.EmployeeID = employees.EmployeeID;

-- 14. List all OrderIDs and the shipper name that the order is going to be shipped via.
SELECT  orders.OrderID, shippers.CompanyName
FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID;

-- 15. List all contries and the total number of orders that are going to be shipped there.
SELECT  ShipCountry, COUNT(ShipCountry) AS total_orders_count
FROM orders
GROUP BY ShipCountry
ORDER BY total_orders_count DESC;

-- 16. Find the employee that has served the most orders.
SELECT e.FirstName, e.LastName, COUNT(o.EmployeeID) AS orders_count
FROM employees AS e  
INNER JOIN orders AS o
ON e.EmployeeID = o.EmployeeID
GROUP BY o.EmployeeID
ORDER BY orders_count DESC
LIMIT 1;

-- 17. Find the customer that has placed the most orders.
SELECT customers.CompanyName, COUNT(orders.CustomerID) AS orders_count
FROM customers
INNER JOIN orders
ON customers.CustomerID = orders.CustomerID
GROUP BY orders.CustomerID
ORDER BY orders_count DESC
LIMIT 1;

-- 18. List all orders, with the employee serving them and the customer, that has placed them.
SELECT orders.OrderID, employees.FirstName, employees.LastName, customers.CompanyName
FROM orders
JOIN employees 
ON orders.EmployeeID = employees.EmployeeID
JOIN customers 
ON orders.CustomerID = customers.CustomerID;

-- 19. List for which customer, which shipper is going to deliver the order.
SELECT orders.OrderID, customers.CompanyName, shippers.CompanyName AS shipper_name
FROM orders
JOIN customers
ON orders.CustomerID = customers.CustomerID
JOIN shippers
ON orders.ShipVia = shippers.ShipperID;
