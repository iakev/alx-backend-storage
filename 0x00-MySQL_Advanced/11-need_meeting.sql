-- Create view on a certain Table
-- create a view listing all students with a score under 80
-- and last meetting equal to NULL or more than 1 month

CREATE VIEW need_meeting
AS SELECT name FROM students
WHERE (score < 80 AND
(MONTH(NOW()) - MONTH(last_meeting) > 1 OR ISNULL(last_meeting)));
