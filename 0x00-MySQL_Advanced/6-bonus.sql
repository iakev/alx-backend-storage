-- Creating a stored procedure
-- Creats a stored procedure that takes in 3 arguments and changes the score of a student

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT,IN project_name VARCHAR(255),IN score INT)
BEGIN
	IF EXISTS(SELECT name FROM projects WHERE name=project_name) THEN
	   INSERT INTO corrections(user_id, project_id, score) VALUES
	   ((SELECT id FROM users WHERE id=user_id), (SELECT id FROM projects WHERE name=project_name), score);
	ELSE
	   INSERT INTO projects (name) VALUES (project_name);
	   INSERT INTO corrections (user_id, project_id, score) VALUES
	   ((SELECT id FROM users WHERE id = user_id), (SELECT id FROM projects WHERE name=project_name), score);  
	END IF;
END;
$$
