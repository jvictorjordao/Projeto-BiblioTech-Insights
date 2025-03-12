CREATE TEMP TABLE sales_att AS
SELECT
	CASE 
		WHEN s.isbn IS NULL THEN split_part(s.sale_date, ',', 1)
	ELSE
		sale_date
	END AS sale_date,
	CASE 
		WHEN s.isbn IS NULL THEN split_part(s.sale_date, ',', 2)
	ELSE
		isbn 
	END AS isbn,
	CASE 
		WHEN s.isbn IS NULL THEN split_part(s.sale_date, '"', 2)
	ELSE
		discount 
	END AS discount,
	CASE 
		WHEN s.isbn IS NULL THEN split_part(s.sale_date, ',', 5)
	ELSE
		item_id 
	END AS item_id,
	CASE 
		WHEN s.isbn IS NULL THEN split_part(s.sale_date, ',', 6)
	ELSE
		order_id 
	END AS order_id
FROM sales s;

SELECT sa.sale_date,
	sa.isbn,
	COUNT(sa.isbn) as "count"
FROM sales_att sa 
GROUP BY sa.isbn, sa.sale_date;

SELECT *
FROM sales_att sa;

