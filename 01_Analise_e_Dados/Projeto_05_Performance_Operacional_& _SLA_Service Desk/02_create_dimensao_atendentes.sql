-- 1. Garante que o banco correto está em uso
USE db_service_desk;


-- 2. Criar a Tabela Dimensão: Dimensao_Atendentes --


CREATE TABLE dimensao_atendentes (
    id_atendente INT PRIMARY KEY AUTO_INCREMENT,
    nome_atendente VARCHAR(100) NOT NULL,
    nivel_atendimento VARCHAR(10) NOT NULL,
    equipe VARCHAR(50) NOT NULL
);

SELECT * FROM dimensao_atendentes;

