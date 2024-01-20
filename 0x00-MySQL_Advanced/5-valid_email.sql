-- This script that creates a trigger that 
-- resets the attribute valid_email only when the email has been changed.
-- Create the trigger
DELIMITER ##
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
-- This section of the code checks if the email is being updated.
    IF NEW.email != OLD.email THEN
-- Set the valid email.
        SET NEW.valid_email = NULL;
	    END IF;
END;
##
DELIMITER ;
