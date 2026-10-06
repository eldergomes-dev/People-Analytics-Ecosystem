-- 1. Criação da Tabela de Funcionários e Histórico de Turnover
CREATE DATABASE IF NOT EXISTS rh_turnover_db;
USE rh_turnover_db;

DROP TABLE IF EXISTS tb_colaboradores;

CREATE TABLE tb_colaboradores (
	id_colaboradores INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL,
    data_admissao DATE NOT NULL,
    data_desligamento DATE NULL,
    status_colaborador VARCHAR(20) DEFAULT 'Ativo', -- 'Ativo' ou 'Desligado'
    tipo_desligamento VARCHAR(30) NULL,				-- 'Volutário' , 'Involuntário' ou NULL
    motivo_desligamento VARCHAR(100) NULL
);

-- 2. Inserção de Dados para Análise de Turnover
INSERT INTO tb_colaboradores
(nome,
departamento,
cargo,
salario,
data_admissao,
data_desligamento,
status_colaborador,
tipo_desligamento,
motivo_desligamento)

VALUES
('Ana Silva','Tecnologia','Desenvolvedor Pleno',7500.00,'2023-01-15',NULL,'Ativo',NULL,NULL),
('Carlos Souza','Tecnologia','Analista de Dados',6200.00,'2022-05-10','2025-11-20','Desligado','Voluntário','Proposta Salarial Maior'),
('Mariana Lima','Vendas','Executivo de Contas',5000.00,'2024-02-01','2025-08-14','Desligado','Voluntário','Insatisfação com Metas'),
('Roberto Alves','Vendas','Gerente de Contas',9500.00,'2021-03-20',NULL,'Ativo',NULL,NULL),
('Fernanda Costa','RH','Business Partner',6800.00,'2022-11-01','2026-01-10','Desligado','Involuntário','Reestruturação da Área'),
('Lucas Pereira','Tecnologia','Desenvolvedor Senior',11000.00,'2020-08-15',NULL,'Ativo',NULL,NULL),
('Juliana Rocha','Marketing','Analista de Marketing',4800.00,'2023-06-01','2025-12-05','Desligado','Voluntário','Mudança de Carreira'),
('Diego Martins','Financeiro','Analista Financeiro',5500.00,'2022-01-10',NULL,'Ativo',NULL,NULL),
('Beatriz Mendes','Vendas','Executivo de Contas',5200.00,'2024-05-12','2026-02-18','Desligado','Voluntário','Proposta Salarial Maior'),
('Thiago Melo','Tecnologia','Devops Engineer',8900.00,'2023-09-01',NULL,'Ativo',NULL,NULL);

-- 3. Query(Consulta) de Consolidação de Métricas de Turnover
SELECT
	departamento,
    COUNT(*) AS total_historico_colaboradores,
    SUM(CASE WHEN status_colaborador = 'Ativo' THEN 1 ELSE 0 END) AS ativos_atuais,
    SUM(CASE WHEN status_colaborador = 'Desligado' THEN 1 ELSE 0 END) AS total_desligados,
    SUM(CASE WHEN tipo_desligamento = 'Voluntário' THEN 1 ELSE 0 END) AS desligamento_voluntarios,
    ROUND((SUM(CASE WHEN status_colaborador = 'Desligado' THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS taxa_turnover_pct
FROM tb_colaboradores
GROUP BY departamento
ORDER BY taxa_turnover_pct DESC;

SELECT * FROM tb_colaboradores; -- Selecionar todos os dados da tabela tb_colaboradores 

