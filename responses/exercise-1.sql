-- Quered in MS SQL Server
-- Exercise 1
-- Given the data sources transactions and order items, write and submit a SQL query that identifies and groups the total amount refunded by location and month. 
SELECT 
	o.locationId AS Location,
	YEAR(CAST(t.date AS DATE)) AS Year,
	MONTH(CAST(t.date AS DATE)) AS Month,
	ROUND(SUM(o.salesAmount), 0) AS TotalRefunded
FROM
	Transactions t
INNER JOIN
	Order_Items o ON t.Id = o.Id
WHERE
	t.type = 'refund'
GROUP BY
	o.locationId,
	YEAR(CAST(t.date AS DATE)),
	MONTH(CAST(t.date AS DATE))
ORDER BY
	Location,
	Year,
	Month;



---- Curiosity led me to see the highest amount of refunds in the most recent year.
---- Grouped by year and highest total amount of refunds

SELECT 
    o.locationId AS Location,
    YEAR(CAST(t.date AS DATE)) AS Year,
    MONTH(CAST(t.date AS DATE)) AS Month,
    ROUND(SUM(o.salesAmount), 0) AS TotalRefunded
FROM
    dbo.Transactions t
INNER JOIN
    dbo.Order_Items o ON t.Id = o.Id
WHERE
    t.type = 'refund'
GROUP BY
    o.locationId,
    YEAR(CAST(t.date AS DATE)),
    MONTH(CAST(t.date AS DATE))
ORDER BY
    Year DESC,
    TotalRefunded DESC;
