-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 
-- An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
	    IN user_id INT
)
BEGIN
-- Begin by calculating the average score for the given user
    DECLARE average_score DECIMAL(10,2);
    START TRANSACTION;
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user_id;

-- After calculating, Update the user's average score
    UPDATE users SET average_score = average_score WHERE id = user_id;
    COMMIT;
END $$

DELIMITER ;
