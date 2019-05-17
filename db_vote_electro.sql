DROP DATABASE IF EXISTS conn_python;


SET NAMES utf8;

CREATE DATABASE conn_python;

USE conn_python;

CREATE TABLE vote_electro(
  id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  pseudo varchar(30) NOT NULL UNIQUE,
  mdp varchar(30) NOT NULL,
  vote int(1) DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO vote_electro (pseudo, mdp, vote)
VALUES ("adri","123",1), ("kama", "123",2),("stuf","123",1), ("talk", "123",3), ("iopp","123",5),
("drog","123",1), ("plon", "123",2),("drit","123",4), ("samm", "123",1), ("crao","123",1);

-- procédure stocké qui récupère les votes de mes 10 profils
DELIMITER | -- Facultatif si votre délimiteur est toujours |
CREATE PROCEDURE compteur_vote()
    -- Définition du paramètre p_espece_id
BEGIN
    SELECT  vote, COUNT(*) AS nb_votant
    FROM vote_electro
    GROUP BY vote ORDER BY vote;
END |
DELIMITER ;  -- On remet le délimiteur par défaut

-- retrouver une procédure stockée :
-- SHOW PROCEDURE STATUS;

