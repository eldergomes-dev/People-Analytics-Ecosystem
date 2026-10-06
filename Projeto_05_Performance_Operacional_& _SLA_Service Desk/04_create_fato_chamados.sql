-- 1. Garante que o banco correto está em uso
USE db_service_desk;


-- 4. Criar a Tabela Fato: Fato_Chamados --

CREATE TABLE fato_chamados (
	id_chamado INT PRIMARY KEY AUTO_INCREMENT,
    id_atendente INT,
    id_categoria INT,
    data_abertura DATETIME NOT NULL,
    data_fechamento DATETIME,
    tempo_resolucao_horas DECIMAL(5,2),
    status_chamado VARCHAR(20) NOT NULL,
    cumpre_sla VARCHAR(3) NOT NULL,
    FOREIGN KEY (id_atendente) REFERENCES dimensao_atendentes(id_atendente),
    FOREIGN KEY (id_categoria) REFERENCES dimensao_categorias(id_categoria)
);

SELECT * FROM fato_chamados;