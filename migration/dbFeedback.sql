CREATE DATABASE IF NOT EXISTS db_feedback;
USE db_feedback;

CREATE TABLE IF NOT EXISTS tb_comentarios(
	cod_comentario int primary key auto_increment,
	nome VARCHAR(150) not null,
    data_hora DATETIME not null,
    comentario text,
	curtidas int
);

CREATE TABLE IF NOT EXISTS tb_comentarios(
	login VARCHAR(40) primary key,
	nome VARCHAR(150) not null,
    senha VARCHAR(20) NOT NULL
);