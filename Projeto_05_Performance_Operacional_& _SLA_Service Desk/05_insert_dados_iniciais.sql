-- 1. Garante que o banco correto está em uso
USE db_service_desk;

-- 5. Inserir Dados Iniciais para Testes --

-- Inserindo Atendentes -- 
INSERT INTO dimensao_atendentes (nome_atendente, nivel_atendimento, equipe) VALUES
('Elder Gomes', 'N3', 'Infraestrutura'),
('Mariana Silva', 'N1', 'Suporte Usuario'),
('Carlos Eduardo', 'N2', 'Sistemas');

-- Inserindo Categorias de SLA --
INSERT INTO dimensao_categorias (nome_categoria, sla_horas_limite) VALUES
('Acessos e Permissoes', 4),	-- Prazo de resolução : até 4 horas
('Hardware e Impressoras', 24),	-- Prazo de resolução : até 24 horas (1 dia útil)
('Instabilidade de Sistema', 8);	-- Prazo de resolução : até 8 horas

-- Inserindo Chamados --
INSERT INTO fato_chamados (id_atendente, id_categoria, data_abertura, data_fechamento, tempo_resolucao_horas, status_chamado, cumpre_sla) VALUES
(1, 3, '2026-05-01 08:00:00', '2026-05-01 12:30:00', 4.50, 'Fechado', 'Sim'),
(2, 1, '2026-05-01 09:15:00', '2026-05-01 15:00:00', 5.75, 'Fechado', 'Nao'),
(3, 2, '2026-05-02 10:00:00', '2026-05-03 09:00:00', 23.00, 'Fechado', 'Sim'),
(1, 3, '2026-05-03 14:00:00', NULL, NULL, 'Em Aberto', 'Nao');

-- Desativa a checagem de chaves estrangeiras --
SET FOREIGN_KEY_CHECKS = 0;

-- Reativa a checagem de chaves estrangeiras --
SET FOREIGN_KEY_CHECKS = 1;


-- Limpa a tabela duplicada --
TRUNCATE TABLE fato_chamados;
TRUNCATE TABLE dimensao_atendentes;
TRUNCATE TABLE dimensao_categorias;


SELECT * FROM dimensao_atendentes;
SELECT * FROM dimensao_categorias;
SELECT * FROM fato_chamados;