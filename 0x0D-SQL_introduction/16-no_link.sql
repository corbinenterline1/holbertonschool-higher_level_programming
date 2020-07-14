-- lists all records of second_table
-- dont' list rows without a name value
-- display score, then name. listed by desc score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
