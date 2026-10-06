-- ============================================================
-- PROJETO 03: VENDAS E-COMMERCE MULTICANAL
-- ARQUIVO: 03_manipulacao_dados_ecommerce.sql
-- OBJETIVO: Evoluir a tabela fato adicionando novas colunas e regras de negócio
-- ============================================================

USE banco_ecommerce;

-- ============================================================
-- 1. ALTERAÇÃO DE ESTRUTURA (DDL) - ADICIONANDO NOVAS COLUNAS
-- ============================================================

-- Adiciona a coluna valor_total_bruto (Quantidade * Valor Unitário)
ALTER TABLE fato_vendas
ADD COLUMN valor_total_bruto DECIMAL(10, 2) AFTER valor_desconto;

-- -- Adiciona a coluna valor_total_liquido (Valor Bruto - Desconto)
ALTER TABLE fato_vendas
ADD COLUMN valor_total_liquido DECIMAL(10, 2) AFTER valor_total_bruto;

-- Adiciona a coluna status_venda (Categoria de avaliação do ticket)
ALTER TABLE fato_vendas
ADD COLUMN status_venda VARCHAR(30) AFTER valor_total_liquido;

-- ============================================================
-- 2. ATUALIZAÇÃO DE DADOS (DML) - PREENCHENDO AS NOVAS COLUNAS
-- ============================================================

-- Desativa o modo de atualização segura para permitir UPDATE na tabela inteira
SET SQL_SAFE_UPDATES = 0;

-- Atualiza os valores calculados de Bruto e Líquido
UPDATE fato_vendas 
SET 
    valor_total_bruto = quantidade * valor_unitario,
    valor_total_liquido = (quantidade * valor_unitario) - valor_desconto;

-- Atualiza os valores calculados de Bruto e Líquido
UPDATE fato_vendas 
SET status_venda = CASE 
    WHEN valor_total_liquido >= 1500.00 THEN 'Ticket Alto'
    WHEN valor_total_liquido >= 500.00 THEN 'Ticket Médio'
    ELSE 'Ticket Baixo'
END;

-- Reativa o modo de atualização segura
SET SQL_SAFE_UPDATES = 1;

-- ============================================================
-- 3. CONSULTA DE VALIDAÇÃO POR COLUNAS
-- ============================================================
SELECT 
    id_venda, 
    quantidade, 
    valor_unitario, 
    valor_desconto, 
    valor_total_bruto, 
    valor_total_liquido, 
    status_venda 
FROM fato_vendas;

-- ============================================================
-- 4. CONSULTA DE VALIDAÇÃO DA TABELA TODA
-- ============================================================
SELECT * FROM fato_vendas;