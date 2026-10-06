-- ==============================================================================
-- PROJETO 04: Análise de Assinaturas e Churn SaaS
-- ARQUIVO: 03_queries_churn_saas.sql
-- DESCRIÇÃO: Consultas de Negócio e Métricas SaaS (MRR, Churn Rate, ARPU, LTV).
-- FINALIDADE: Calcular os indicadores-chave de desempenho (KPIs) para medir
--             a saúde financeira e a retenção de clientes.
-- ESTILO: Nomes literais das tabelas (sem apelidos/aliases), garantindo
--         referenciamento direto de cada campo.
-- ==============================================================================

USE db_saas_analytics;

-- 1. RECEITA RECORRENTE MENSAL (MRR - Monthly Recurring Revenue)
-- Soma o valor mensal dos planos de todos os clientes com assinaturas ativas
SELECT 
    SUM(tb_planos.valor_mensal) AS receita_recorrente_mensal_mrr,
    COUNT(tb_assinaturas.id_assinatura) AS total_assinantes_ativos
FROM tb_assinaturas 
JOIN tb_planos 
    ON tb_assinaturas.id_plano = tb_planos.id_plano
WHERE tb_assinaturas.status_assinatura = 'Ativo';


-- 2. TAXA DE CANCELAMENTO DE CLIENTES (Churn Rate %)
-- Percentual de clientes que cancelaram a assinatura em relação ao total de contratos
SELECT 
    COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) AS total_cancelamentos_churn,
    COUNT(*) AS total_clientes_historico,
    ROUND((COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) / COUNT(*)) * 100, 2) AS taxa_churn_percentual
FROM tb_assinaturas;


-- 3. RECEITA MÉDIA POR USUÁRIO (ARPU - Average Revenue Per User)
-- Média do valor pago mensalmente por cada cliente com assinatura ativa
SELECT 
    ROUND(SUM(tb_planos.valor_mensal) / COUNT(tb_assinaturas.id_assinatura), 2) AS receita_media_por_usuario_arpu
FROM tb_assinaturas
JOIN tb_planos 
    ON tb_assinaturas.id_plano = tb_planos.id_plano
WHERE tb_assinaturas.status_assinatura = 'Ativo';


-- 4. DISTRIBUIÇÃO DE RECEITA E CANCELAMENTOS POR TIPO DE PLANO
-- Identifica quais planos geram maior receita e em quais ocorre maior cancelamento
SELECT 
    tb_planos.nome_plano,
    COUNT(tb_assinaturas.id_assinatura) AS total_contratos_historico,
    SUM(CASE WHEN tb_assinaturas.status_assinatura = 'Ativo' THEN tb_planos.valor_mensal ELSE 0 END) AS receita_mensal_por_plano,
    COUNT(CASE WHEN tb_assinaturas.status_assinatura = 'Cancelado' THEN 1 END) AS total_cancelamentos_por_plano
FROM tb_planos
LEFT JOIN tb_assinaturas 
    ON tb_planos.id_plano = tb_assinaturas.id_plano
GROUP BY tb_planos.id_plano, tb_planos.nome_plano
ORDER BY receita_mensal_por_plano DESC;


-- 5. LIFETIME VALUE (LTV - Valor Total Gerado por Cliente)
-- Soma do valor total pago e aprovado por cada cliente ao longo do tempo de contrato
SELECT 
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
GROUP BY tb_clientes.id_cliente, tb_clientes.nome, tb_planos.nome_plano
ORDER BY valor_total_historico_ltv DESC;