-- Create a stored procedure that computes average score
-- Compute average given a userid from corrections, update the average score on users

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET users.average_score =
	(SELECT SUM(score)/COUNT(*) FROM corrections WHERE corrections.user_id=user_id)
	WHERE id = user_id;
END;
$$
