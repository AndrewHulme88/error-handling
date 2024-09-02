SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_amount_spent
FROM
    customers c
JOIN
    orders o ON c.customer_id = o.customer_id
JOIN
    products p ON o.product_id = p.product_id
WHERE
    p.category = 'Guitar' AND
    o.order_date BETWEEN '2022-01-01' AND '2023-01-01'
GROUP BY
    c.customer_id, c.first_name, c.last_name
ORDER BY
    total_amount_spent DESC;
