-- Active: 1788892538974@@127.0.0.1@3306@db_service_desk
-- 1. Garante que o banco correto está em uso
USE db_service_desk;


-- Criar a Tabela Dimensão: Dimensao_Categorias --

CREATE TABLE dimensao_categorias (
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(100) NOT NULL,
    sla_horas_limite INT NOT NULL
);
    
SELECT * FROM dimensao_categorias;