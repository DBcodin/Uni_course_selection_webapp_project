/*CREATE DATABASE Secure_database;*/


USE Secure_database;

CREATE TABLE Secure_records (
 /*Name_column VARCHAR (255)  I AM CURRENTLY ABOUT TO DELETE THIS */
 );

SELECT * FROM Secure_records;

/*DELETE FROM polls_question WHERE id = 2;*/

DROP TABLE Secure_records;
/*DROP COLUMN Name_column;*/

	SELECT * FROM polls_moduleinfo;
    SELECT * FROM polls_modulelinking;
    SELECT * FROM polls_usermoduleinfo;
    
    SELECT * FROM polls_choice;
    SELECT * FROM polls_question;
    
    
    /*UPDATE polls_modulelinking
	SET Link_Module_code= 'WSB010', Followed_by= 'WSA023', Precursed_by= 'WSC311'
	WHERE id = ;   NOT NEEDED YET DUE TO ISSUE WITH ENTERING NOT BEING SAVED*/