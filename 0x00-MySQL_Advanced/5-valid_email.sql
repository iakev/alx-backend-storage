-- A script that creates a trigger on an UPDATE event
-- Create a Trigger on users table;

DELIMITER $$ ;
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END;
$$
