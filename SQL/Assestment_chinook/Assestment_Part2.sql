-- 1. Show all the details of the products that have a price greater than 100. 
SELECT * 
FROM Product
WHERE price > 100
ORDER by price ASC;


-- 2. Show all the products along with the supplier detail who supplied the products. 
SELECT p.product_id, p.product_name, p.genre, p.type, p.price, s.supplier_id, s.supplier_name, s.contact
FROM product p
JOIN supplier s on s.supplier_id = p.supplier_id

-- 3. Show all the products bought by the top 5 customers (the customers that spent the  most in the store).
SELECT st.customer_id, c.customer_name, p.product_name
FROM sales_transaction st
JOIN sales_items si on st.invoice_id = si.invoice_id
JOIN product p on p.product_id = si.product_id
JOIN customer c on st.customer_id = c.customer_id
WHERE st.customer_id IN (
	SELECT st.customer_id
	FROM sales_transaction st
	GROUP by customer_id
	ORDER by sum(total) DESC
	Limit 5
)
ORDER by st.customer_id ASC

-- 4. Show the information of the top 3 suppliers with more products. 
SELECT product.supplier_id, supplier.supplier_name, count(product.supplier_id) Product_Count, supplier.contact
FROM product
JOIN supplier on supplier.supplier_id = product.supplier_id
GROUP by product.supplier_id
ORDER by Product_Count DESC
LIMIT 3

-- 5. What is the product with the highest value of sales? 
SELECT p.product_id, p.product_name, p.genre, p.type, p.price * sum(si.quantity) as total_sold
FROM sales_items si
JOIN sales_transaction st on st.invoice_id = si.invoice_id
JOIN product p on p.product_id = si.product_id
GROUP by si.product_id
ORDER by total_sold DESC
LIMIT 1

-- 6. Sum the total sales by month.
SELECT strftime('%m', date) AS Month, SUM(total) AS TotalSales
FROM Sales_Transaction
GROUP BY strftime('%m', date)
ORDER BY strftime('%m', date)

-- 7. Create a view that shows the total number of items a customer bought
-- from the business in October 2023 along with the total price. 
CREATE VIEW OctoberPurchases AS
SELECT c.customer_id CustomerID, c.customer_name, count(si.quantity) NumberOfItems, sum(p.price * si.quantity) TotalPrice
FROM sales_items si
JOIN sales_transaction st on st.invoice_id = si.invoice_id
JOIN customer c on c.customer_id = st.customer_id
JOIN product p on p.product_id = si.product_id
WHERE st.date BETWEEN '2023-10-01' AND '2023-10-31'
GROUP by c.customer_id

-- 8. Delete all customers who never bought a product from the business. 
DELETE FROM customer
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id
    FROM sales_transaction
)

-- 9. List all the customers whose name starts with B.
SELECT * 
FROM customer 
WHERE customer_name 
LIKE 'B%'

-- 10. What supplier sold more products?
SELECT p.supplier_id, s.supplier_name, sum(si.quantity) products_sold
FROM product p
JOIN sales_items si on si.product_id = p.product_id
JOIN supplier s on s.supplier_id = p.supplier_id
GROUP by p.supplier_id
ORDER by products_sold DESC
LIMIT 1

