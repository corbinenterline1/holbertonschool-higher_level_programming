-- lists all the cities of Cali in database.
-- sort ascending by cities.id, no JOIN
SELECT id, name FROM cities WHERE state_id IN (
	SELECT id FROM states WHERE name = "California");
