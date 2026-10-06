-- ============================================================
-- PROJETO 03: VENDAS E-COMMERCE MULTICANAL
-- ARQUIVO: 02_inserir_dados_ecommerce.sql
-- OBJETIVO: Inserir dados fictícios nas tabelas Dimensão e Fato
-- ============================================================

USE banco_ecommerce;

-- ============================================================
-- 1. POPULANDO AS TABELAS DIMENSÃO (CADASTROS)
-- ============================================================

-- Inserindo Clientes
INSERT INTO dim_clientes (nome_cliente, cidade, estado, segmento) VALUES
('Elder gomes', 'São Paulo', 'SP', 'Corporativo'),
('Ana Silva', 'Rio de Janeiro', 'RJ', 'Varejo'),
('Carlos Oliveira', 'Belo Horizonte', 'MG', 'Varejo'),
('Mariana Santos', 'Curitiba', 'PR', 'Corporativo'),
('Roberto Souza', 'Porto Alegre', 'RS', 'Varejo');

-- Inserindo Produtos
INSERT INTO dim_produtos (nome_produto, categoria, preco_tabela) VALUES
('Teclado Mecânico RGB', 'Periféricos', 250.00),
('Mouse Sem Fio Ergônomico', 'Periféricos', 120.00),
('Monitor 27 Polegadas 4K', 'Monitores', 1800.00),
('Cadeira Ergonômica', 'Móveis', 950.00),
('Headset Gamer 7.1', 'Áudio', 350.00);

-- Inserindo Canais de Venda
INSERT INTO dim_canais (nome_canal) VALUES
('Website'),
('Aplicativo Mobile'),
('Loja Física'),
('Marketplace');

-- ============================================================
-- 2. POPULANDO A TABELA FATO (TRANSAÇÕES DE VENDAS)
-- ============================================================

-- Inserindo Registros de Vendas
-- (id_cliente, id_produto e id_canal usam os IDs gerados nas tabelas acima)
INSERT INTO fato_vendas (data_venda, id_cliente, id_produto, id_canal, quantidade, valor_unitario, valor_desconto) VALUES
('2026-08-01', 1, 3, 1, 1, 1800.00, 100.00), -- Elder comprou Monitor no Site
('2026-08-02', 2, 1, 2, 2, 250.00, 20.00),   -- Ana comprou 2 Teclados no App
('2026-08-03', 3, 4, 3, 1, 950.00, 50.00),   -- Carlos comprou Cadeira na Loja Física
('2026-08-04', 4, 2, 4, 3, 120.00, 0.00),    -- Mariana comprou 3 Mouses no Marketplace
('2026-08-05', 5, 5, 1, 1, 350.00, 15.00),   -- Roberto comprou Headset no Site
('2026-08-06', 1, 1, 2, 1, 250.00, 0.00),    -- Elder comprou Teclado no App
('2026-08-07', 2, 3, 1, 1, 1800.00, 150.00), -- Ana comprou Monitor no Site
('2026-08-08', 3, 5, 4, 2, 350.00, 30.00);   -- Carlos comprou 2 Headsets no Marketplace

SELECT * FROM dim_clientes;
SELECT * FROM dim_produtos;
SELECT * FROM dim_canais;
SELECT * FROM fato_vendas;


-- Desativa o modo de atualização segura para permitir UPDATE na tabela inteira
SET SQL_SAFE_UPDATES = 0;

-- Reativa o modo de atualização segura
SET SQL_SAFE_UPDATES = 1;

