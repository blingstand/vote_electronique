DROP DATABASE IF EXISTS conn_python;
DROP TABLE IF EXISTS vote_electro;

SET NAMES utf8;

CREATE DATABASE conn_python;

USE conn_python;

CREATE TABLE vote_electro(
  id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  pseudo varchar(30) NOT NULL UNIQUE,
  mdp varchar(30) NOT NULL,
  vote varchar(50) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
