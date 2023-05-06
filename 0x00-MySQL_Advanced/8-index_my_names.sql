-- Creae an index on an fields starting letter
-- Index to help querying be better

CREATE INDEX idx_name_first ON names (name(1));
