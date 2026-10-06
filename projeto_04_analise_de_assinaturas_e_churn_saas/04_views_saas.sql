-- ==============================================================================
-- PROJETO 04: Análise de Assinaturas e Churn SaaS
-- ARQUIVO: 04_views_saas.sql
-- DESCRIÇÃO: Criação de Views (Tabelas Virtuais) para Métricas de Negócio.
-- FINALIDADE: Disponibilizar as métricas de MRR, Churn e LTV de forma simples
--             para consumo em ferramentas de BI (Power BI) e relatórios.
-- ESTILO: Referenciamento direto das tabelas (sem apelidos/aliases), priorizando
--         a leitura imediata e a clareza do código a olho nu.
-- ==============================================================================

USE db_saas_analytics;

-- 1. VIEW DE RESUMO DO MRR E ASSINANTES ATIVOS
-- Permite consultar o valor atual da Receita Recorrente Mensal de forma direta

CREATE OR REPLACE VIEW vw_mrr_atual AS
SELECT 
    SUM(tb_planos.valor_mensal) AS receita_recorrente_mensal_mrr,
    COUNT(tb_assinaturas.id_assinatura) AS total_assinantes_ativos
FROM tb_assinaturas
JOIN tb_planos 
    ON tb_assinaturas.id_plano = tb_planos.id_plano
WHERE tb_assinaturas.status_assinatura = 'Ativo';

-- 2. VIEW DE INDICADORES DE CHURN (CANCELAMENTO)
-- Exibe o total de cancelamentos e a taxa percentual de perda de clientes
CREATE OR REPLACE VIEW vw_mudar_churn_rate AS
SELECT 
    COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) AS total_cancelamentos_churn,
    COUNT(*) AS total_clientes_historico,
    ROUND((COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) / COUNT(*)) * 100, 2) AS taxa_churn_percentual
FROM tb_assinaturas;

-- 3. VIEW DE DESEMPENHO E RECEITA POR PLANO
-- Consolida a performance financeira e o volume de cancelamentos de cada plano
CREATE OR REPLACE VIEW vw_desempenho_planos AS
SELECT 
    tb_planos.id_plano,
    tb_planos.nome_plano,
    tb_planos.valor_mensal,
    COUNT(tb_assinaturas.id_assinatura) AS total_contratos_historico,
    SUM(CASE WHEN tb_assinaturas.status_assinatura = 'Ativo' THEN tb_planos.valor_mensal ELSE 0 END) AS receita_mensal_por_plano,
    COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) AS total_cancelamentos_por_plano
FROM tb_planos
LEFT JOIN tb_assinaturas 
    ON tb_planos.id_plano = tb_assinaturas.id_plano
GROUP BY tb_planos.id_plano, tb_planos.nome_plano, tb_planos.valor_mensal;

-- 4. VIEW DE LIFETIME VALUE (LTV) POR CLIENTE
-- Agrega todo o valor financeiro efetivamente pago e aprovado por cliente
CREATE OR REPLACE VIEW vw_ltv_clientes AS
SELECT 
    tb_clientes.id_cliente,
    tb_clientes.nome AS nome_cliente,
    tb_planos.nome_plano,
    SUM(tb_pagamentos.valor_pago) AS valor_total_historico_ltv
FROM tb_clientes
JOIN tb_assinaturas 
    ON tb_clientes.id_cliente = tb_assinaturas.id_cliente
JOIN tb_planos 
    ON tb_assinaturas.id_plano = tb_planos.id_plano
JOIN tb_pagamentos 
    ON tb_assinaturas.id_assinatura = tb_pagamentos.id_assinatura
WHERE tb_pagamentos.status_pagamento = 'Aprovado'
GROUP BY tb_clientes.id_cliente, tb_clientes.nome, tb_planos.nome_plano;

SELECT * FROM vw_mrr_atual;
SELECT * FROM vw_desempenho_planos;