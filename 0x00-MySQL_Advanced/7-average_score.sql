-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE avg_score DECIMAL(10, 2);

	-- Compute the average score
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;

	-- Update the average score in the user table
	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END$$
DELIMITER ;
