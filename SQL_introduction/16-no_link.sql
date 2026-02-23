-- 16. Say my name
-- Lists all records from second_table with a non-NULL name, ordered by score (desc).
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
