SELECT SUM(amount) AS total_sales_march_2024
FROM orders
WHERE strftime('%Y-%m', order_date) = '2024-03';




SELECT customer, SUM(amount) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;



SELECT AVG(amount) AS avg_order_last_3_months
FROM orders
WHERE order_date >= date('now', '-3 months');
