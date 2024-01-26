-- This SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student
-- Start by calculatin the weighted scores for each correction
-- Next calculate the total weight of all corrections
-- Then finally compute the the average weighted score.
-- Remember to take care of the divide by zero error

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	    IN user_id INT
)
BEGIN
	    DECLARE total_weighted_score DECIMAL(10,2) DEFAULT 0;
	    DECLARE total_weight INT DEFAULT 0;
    
    SELECT SUM(score * weight) INTO total_weighted_score
    FROM corrections
    WHERE user_id = user_id;

    SELECT SUM(weight) INTO total_weight
    FROM corrections
    WHERE user_id = user_id;

    IF total_weight = 0 THEN
	        SET total_weighted_score = 0;
		    ELSE
			        SET total_weighted_score = total_weighted_score / total_weight;
				    END IF;

    UPDATE users SET average_weighted_score = total_weighted_score WHERE id = user_id;
END $$

DELIMITER ;
