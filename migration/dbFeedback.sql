CREATE DATABASE IF NOT EXISTS dbFeedback;
USE dbFeedback;

CREATE TABLE IF NOT EXISTS tbComentarios(
	idComentario int primary key auto_increment,
	nome VARCHAR(150) not null,
    dataHora DATETIME not null,
    comentario text
);