-- creates table force_name
-- shall not fail, gotta have a name
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
)
