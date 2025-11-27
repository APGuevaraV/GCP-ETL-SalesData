--save as view

SELECT *,(Quantity*UnitPrice) as total_sales FROM `sales.orders` order by country

SELECT *,(Quantity*UnitPrice) as total_sales FROM `sales.orders` where country = 'Germany'

SELECT *,(Quantity*UnitPrice) as total_sales FROM `sales.orders` where country = 'USA'

SELECT *,(Quantity*UnitPrice) as total_sales FROM `windy-lyceum-475920-n3.sales.orders` where country = 'United Kingdom'