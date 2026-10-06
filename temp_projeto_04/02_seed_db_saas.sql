USE db_saas_analytics;

-- 1. POVOAMENTO DA TABELA DE PLANOS (Dimensão de Ofertas)
INSERT INTO tb_planos (id_plano, nome_plano, valor_mensal, limite_usuarios) VALUES
(1, 'Basic', 49.90, 3),
(2, 'Pro', 149.90, 10),
(3, 'Enterprise', 499.90, 50)
AS novos_planos
ON DUPLICATE KEY UPDATE nome_plano = novos_planos.nome_plano;

-- 2. POVOAMENTO DA TABELA DE CLIENTES (Dimensão de Usuários)
INSERT INTO tb_clientes (id_cliente, nome, email, pais, data_cadastro) VALUES
(1, 'TechCorp Solucoes', 'contato@techcorp.com', 'Brasil', '2025-01-10 09:00:00'),
(2, 'Inovacao Digital LTDA', 'financeiro@inovacao.com', 'Brasil', '2025-01-15 14:30:00'),
(3, 'Global Soft Inc', 'admin@globalsoft.com', 'Portugal', '2025-02-01 11:15:00'),
(4, 'Alpha Analytics', 'suporte@alphaanalytics.com', 'Brasil', '2025-02-20 16:45:00'),
(5, 'Beta Logistics', 'operacoes@betalog.com', 'Espanha', '2025-03-05 10:00:00')
AS novos_clientes
ON DUPLICATE KEY UPDATE nome = novos_clientes.nome;

-- 3. POVOAMENTO DA TABELA DE ASSINATURAS (Fato de Contratos)
INSERT INTO tb_assinaturas (id_assinatura, id_cliente, id_plano, data_inicio, data_cancelamento, status_assinatura) VALUES
(1, 1, 2, '2025-01-10 09:30:00', NULL, 'Ativo'),                   -- Cliente 1 no plano Pro (Ativo)
(2, 2, 1, '2025-01-15 15:00:00', '2025-04-15 10:00:00', 'Cancelado'), -- Cliente 2 no Basic (Cancelou - CHURN)
(3, 3, 3, '2025-02-01 11:30:00', NULL, 'Ativo'),                   -- Cliente 3 no Enterprise (Ativo)
(4, 4, 1, '2025-02-20 17:00:00', NULL, 'Ativo'),                   -- Cliente 4 no Basic (Ativo)
(5, 5, 2, '2025-03-05 10:30:00', '2025-05-10 18:20:00', 'Cancelado')  -- Cliente 5 no Pro (Cancelou - CHURN)
AS novas_assinaturas
ON DUPLICATE KEY UPDATE status_assinatura = novas_assinaturas.status_assinatura;

-- 4. POVOAMENTO DA TABELA DE PAGAMENTOS (Fato Financeira)
INSERT INTO tb_pagamentos (id_pagamento, id_assinatura, data_pagamento, valor_pago, status_pagamento) VALUES
-- Pagamentos Cliente 1 (Pro - 149.90)
(1, 1, '2025-01-10 09:35:00', 149.90, 'Aprovado'),
(2, 1, '2025-02-10 09:00:00', 149.90, 'Aprovado'),
(3, 1, '2025-03-10 09:00:00', 149.90, 'Aprovado'),

-- Pagamentos Cliente 2 (Basic - 49.90)
(4, 2, '2025-01-15 15:05:00', 49.90, 'Aprovado'),
(5, 2, '2025-02-15 09:00:00', 49.90, 'Aprovado'),
(6, 2, '2025-03-15 09:00:00', 49.90, 'Aprovado'),

-- Pagamentos Cliente 3 (Enterprise - 499.90)
(7, 3, '2025-02-01 11:35:00', 499.90, 'Aprovado'),
(8, 3, '2025-03-01 09:00:00', 499.90, 'Aprovado'),

-- Pagamentos Cliente 4 (Basic - 49.90)
(9, 4, '2025-02-20 17:05:00', 49.90, 'Aprovado'),

-- Pagamentos Cliente 5 (Pro - 149.90)
(10, 5, '2025-03-05 10:35:00', 149.90, 'Aprovado')
AS novos_pagamentos
ON DUPLICATE KEY UPDATE status_pagamento = novos_pagamentos.status_pagamento;

-- Validação de Carga
SELECT * FROM tb_pagamentos;

