-- create a complex index
-- create an index on first letter of name and score too

CREATE INDEX idx_name_first_score ON names (name(1), score);
