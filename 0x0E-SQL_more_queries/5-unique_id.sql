-- Creates the table unique_id on MySQL.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT, DEFAULT 1 UNIQUE, name VARCHAR(256)
);

-- flush the privilages to include changes
FLUSH PRIVILAGES;
