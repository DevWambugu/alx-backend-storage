-- This script creates a stored procedure AddBonus 
-- that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus(
	    IN user_id INT,
	    IN project_name VARCHAR(255),
	    IN score INT
)
BEGIN
    -- First step, Check if the project already exists
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If the project doesn't exist, create it
    IF project_id IS NULL THEN
	        INSERT INTO projects (name) VALUES (project_name);
		        SET project_id = LAST_INSERT_ID();
			    END IF;

    -- Add the update to the table
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$

DELIMITER ;
