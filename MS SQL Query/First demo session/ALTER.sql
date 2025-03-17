ALTER TABLE anime 
ADD anime_mc VARCHAR(20) NOT NULL

SELECT name FROM sys.key_constraints 

ALTER TABLE anime
ADD CONSTRAINT primarykey7 PRIMARY KEY (anime_id)

ALTER TABLE anime 
DROP CONSTRAINT PK__anime__1D82A06A9CBC8D65

ALTER TABLE anime
DROP COLUMN anime_id

SELECT * FROM anime

INSERT INTO anime
VALUES
	(1, 'bleach', 'ichigo'),
	(2, 'hunter x hunter', 'gon')