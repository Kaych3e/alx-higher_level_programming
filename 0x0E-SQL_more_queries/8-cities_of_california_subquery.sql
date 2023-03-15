-- Lists all cities of California that can be found in database 'hbtn_0d_usa'
-- 'states' table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
SELECT id, name FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = 'California');