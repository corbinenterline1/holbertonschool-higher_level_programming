-- creates table unique_id
-- shall not fail, id default 1, must be unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
)
