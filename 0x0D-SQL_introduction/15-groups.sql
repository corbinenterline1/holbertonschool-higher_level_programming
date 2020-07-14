-- lists number of records with same score in second_table
-- displays score, number of records for this score with the label number
-- sorted by number of records (desc)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
