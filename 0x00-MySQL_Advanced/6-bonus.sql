-- Creates a stored procedure AddBonus that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
	user_id INT,
	project_name VARCHAR(255),
	score FLOAT
)
BEGIN
	DECLARE project_id INT;

	-- Check if the projects exists
	SELECT id INTO project_id FROM projects WHERE name = project_name;
	
	-- If the project doesn't exist, create it
	IF project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Insert the correction
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$
DELIMITER ;
