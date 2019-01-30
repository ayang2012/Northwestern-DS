use sakila;

-- 1a
SELECT first_name, last_name
FROM actor;

-- 1b
SELECT UPPER(CONCAT(first_name, " ", last_name)) `Actor Name`
FROM actor;

-- 2a
SELECT actor_id
FROM actor
WHERE first_name LIKE "Joe";

-- 2c
SELECT *
FROM actor
WHERE last_name LIKE "%li%"
ORDER BY last_name, first_name;

-- 2d
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a
ALTER TABLE actor
ADD description BLOB;

-- 3b
ALTER TABLE actor
DROP description;

-- 4a
SELECT last_name, count(last_name) count
FROM actor
GROUP BY last_name;

-- 4b
SELECT last_name, count(last_name) count
FROM actor
GROUP BY last_name
HAVING count(last_name) >=2;

-- 4c
UPDATE actor
SET first_name = "GROUCHO", last_name = "WILLIAMS"
WHERE first_name = "HARPO" and last_name = "WILLIAMS";

-- 4d
UPDATE actor
SET first_name = "HARPO"
WHERE first_name = "GROUCHO";

-- 5a
CREATE TABLE address (
  address_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  address VARCHAR(50) NOT NULL,
  address2 VARCHAR(50) DEFAULT NULL,
  district VARCHAR(20) NOT NULL,
  city_id SMALLINT UNSIGNED NOT NULL,
  postal_code VARCHAR(10) DEFAULT NULL,
  phone VARCHAR(20) NOT NULL,
  /*!50705 location GEOMETRY NOT NULL,*/
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (address_id),
  KEY idx_fk_city_id (city_id),
  /*!50705 SPATIAL KEY `idx_location` (location),*/
  CONSTRAINT `fk_address_city` FOREIGN KEY (city_id) REFERENCES city (city_id) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 6a
SELECT staff.first_name, staff.last_name, address.address
FROM staff
JOIN address
ON staff.address_id = address.address_id;

-- 6b
SELECT staff.first_name, staff.last_name, count(*) 
FROM payment
JOIN staff
ON payment.staff_id = staff.staff_id
GROUP BY staff.staff_id;

-- 6c
SELECT film.title, count(film_actor.actor_id) 
FROM film_actor
JOIN film
ON film.film_id = film_actor.film_id
GROUP BY film.title;

-- 6d
SELECT film.title, count(*)
FROM film
JOIN inventory
ON film.film_id = inventory.film_id
WHERE film.title = "Hunchback Impossible"
GROUP BY film.title;

-- 6e
SELECT customer.first_name, customer.last_name, sum(payment.amount)
FROM payment
JOIN customer
ON payment.customer_id = customer.customer_id
GROUP BY customer.first_name, customer.last_name
ORDER BY customer.first_name, customer.last_name;

-- 7a
SELECT title 
FROM film
WHERE (title LIKE "K%" OR title LIKE "Q%") 
	AND language_id = 
		(SELECT language_id
		FROM language
		WHERE name = "English")
;

-- 7b
SELECT first_name, last_name
FROM film_actor
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film_id =
	(SELECT film_id
	FROM film
	WHERE title = "Alone Trip")
;

-- 7c
SELECT first_name, last_name, email
FROM customer
WHERE address_id IN
	(SELECT address_id
	FROM address
	WHERE city_id IN
		(SELECT city.city_id
		FROM address
		JOIN city
		ON city.city_id = address.city_id
		WHERE country_id = 
			(SELECT country_id
			FROM country
			WHERE country = 'Canada')))
;

-- 7d
SELECT *
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
WHERE category_id = 
	(SELECT category_id 
	FROM category
	WHERE name = 'Family')
;

-- 7e
SELECT title, number_of_rentals
FROM film
JOIN (
	SELECT film_id, count(*) as number_of_rentals
	FROM inventory
	JOIN rental
	ON rental.inventory_id = inventory.inventory_id
	GROUP BY film_id) as joined
ON film.film_id = joined.film_id
ORDER BY number_of_rentals DESC
;

-- 7f
SELECT store_id, sum(revenue) 
FROM inventory
JOIN (SELECT inventory_id, sum(amount) as revenue
	FROM payment
	JOIN rental
	ON payment.rental_id = rental.rental_id
	GROUP BY inventory_id) as joined
ON inventory.inventory_id=joined.inventory_id
GROUP BY store_id
;

-- 7g
SELECT store_id, city, country 
FROM (SELECT store_id, city_id 
	FROM store
	JOIN address
	ON store.address_id = address.address_id) as tab1
JOIN (SELECT city_id, city, country
	FROM city
	JOIN country
	on city.country_id=country.country_id) as tab2
ON tab1.city_id=tab2.city_id
;

-- 7h
SELECT name, sum(revenue)
FROM (SELECT film_id, revenue
	FROM inventory
	JOIN (SELECT inventory_id, sum(amount) as revenue
		FROM payment
		JOIN rental
		ON payment.rental_id = rental.rental_id
		GROUP BY inventory_id) as joined
	ON inventory.inventory_id=joined.inventory_id) as tab1
JOIN film
ON tab1.film_id = film.film_id
JOIN film_category
ON film.film_id=film_category.film_id
JOIN category
ON category.category_id=film_category.category_id
GROUP BY name
ORDER BY sum(revenue) DESC
LIMIT 5
;


-- 8a
CREATE VIEW `Top 5 Gross Category` AS
SELECT name, sum(revenue)
FROM (SELECT film_id, revenue
	FROM inventory
	JOIN (SELECT inventory_id, sum(amount) as revenue
		FROM payment
		JOIN rental
		ON payment.rental_id = rental.rental_id
		GROUP BY inventory_id) as joined
	ON inventory.inventory_id=joined.inventory_id) as tab1
JOIN film
ON tab1.film_id = film.film_id
JOIN film_category
ON film.film_id=film_category.film_id
JOIN category
ON category.category_id=film_category.category_id
GROUP BY name
ORDER BY sum(revenue) DESC
LIMIT 5
;


-- 8b
SELECT * FROM `Top 5 Gross Category`;

-- 8c
DROP VIEW `Top 5 Gross Category`;

