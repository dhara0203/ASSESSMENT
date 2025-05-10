CREATE DATABASE  CONTRY;
USE CONTRY;
country_id (PK), country_name
city_id (PK), city_name, country_id (FK to country)
customer_id (PK), customer_name, city_id (FK to city)
SELECT 
    customer.customer_id,
    customer.customer_name,
    city.city_name,
    country.country_name
FROM 
    customer
JOIN 
    city ON customer.city_id = city.city_id
JOIN 
    country ON city.country_id = country.country_id;
    
/*country(country_id, country_name)

city(city_id, city_name, country_id)

customer(customer_id, customer_name, city_id)*/
SELECT 
    country.country_name,
    city.city_name,
    customer.customer_name
FROM 
    country
LEFT JOIN 
    city ON country.country_id = city.country_id
LEFT JOIN 
    customer ON city.city_id = customer.city_id;


