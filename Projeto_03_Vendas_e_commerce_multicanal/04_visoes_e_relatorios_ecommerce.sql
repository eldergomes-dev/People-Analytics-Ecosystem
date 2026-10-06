-- ============================================================
-- PROJETO 03: VENDAS E-COMMERCE MULTICANAL
-- ARQUIVO: 04_visoes_e_relatorios_ecommerce.sql
-- OBJETIVO: Criar Views relacionando Fato e Dimensões sem uso de apelidos
-- ============================================================

USE banco_ecommerce;

-- ============================================================
-- 1. CRIAÇÃO DA VIEW CONSOLIDADA DE VENDAS
-- ============================================================

-- CREATE OR REPLACE VIEW: Cria a visão ou substitui caso ela já exista
CREATE OR REPLACE VIEW vw_vendas_consolidadas AS
SELECT 
    fato_vendas.id_venda,                               -- Identificador único da venda (Tabela Fato)
    fato_vendas.data_venda,                             -- Data do registro da venda (Tabela Fato)
    dim_clientes.nome_cliente,                          -- Nome completo do cliente (Tabela Dimensão Cliente)
    dim_clientes.cidade AS cidade_cliente,              -- Cidade de residência do cliente
    dim_clientes.estado AS estado_cliente,              -- Estado do cliente (ex: SP, RJ)
    dim_clientes.segmento AS segmento_cliente,          -- Segmento do cliente (ex: Varejo, Corporativo)
    dim_produtos.nome_produto,                          -- Nome do produto vendido (Tabela Dimensão Produto)
    dim_produtos.categoria AS categoria_produto,        -- Categoria do produto (ex: Periféricos, Monitores)
    dim_canais.nome_canal,                              -- Nome do meio de venda (Tabela Dimensão Canal)
    fato_vendas.quantidade,                             -- Quantidade vendida de itens
    fato_vendas.valor_unitario,                         -- Preço por unidade praticado na venda
    fato_vendas.valor_desconto,                         -- Desconto total concedido
    fato_vendas.valor_total_bruto,                      -- Valor bruto da venda (Quantidade * Valor Unitário)
    fato_vendas.valor_total_liquido,                    -- Valor líquido final (Valor Bruto - Desconto)
    fato_vendas.status_venda                            -- Classificação do ticket (Alto, Médio, Baixo)
FROM fato_vendas
INNER JOIN dim_clientes 
    ON fato_vendas.id_cliente = dim_clientes.id_cliente  -- Relacionamento: Fato Vendas com Dimensão Clientes
INNER JOIN dim_produtos 
    ON fato_vendas.id_produto = dim_produtos.id_produto  -- Relacionamento: Fato Vendas com Dimensão Produtos
INNER JOIN dim_canais 
    ON fato_vendas.id_canal = dim_canais.id_canal;       -- Relacionamento: Fato Vendas com Dimensão Canais

-- ============================================================
-- 2. CRIAÇÃO DA VIEW DE RESUMO POR CANAL DE VENDA
-- ============================================================

CREATE OR REPLACE VIEW vw_resumo_por_canal AS
SELECT 
    dim_canais.nome_canal,                                               -- Nome do canal de venda
    COUNT(fato_vendas.id_venda) AS total_pedidos,                        -- Contagem total de transações registradas
    SUM(fato_vendas.quantidade) AS quantidade_total_itens,               -- Soma do volume total de itens vendidos
    SUM(fato_vendas.valor_total_liquido) AS faturamento_total_liquido    -- Soma do faturamento líquido total acumulado
FROM fato_vendas
INNER JOIN dim_canais 
    ON fato_vendas.id_canal = dim_canais.id_canal                       -- Relacionamento: Fato Vendas com Dimensão Canais
GROUP BY dim_canais.nome_canal;                                          -- Agrupamento dos totais por nome de cada canal

-- ============================================================
-- 3. CONSULTAS DE TESTE E VALIDAÇÃO DAS VIEWS
-- ============================================================

-- Consulta 1: Retorna a visão completa consolidada com todos os nomes claros
SELECT * FROM vw_vendas_consolidadas;

-- Consulta 2: Retorna o resumo agrupado de faturamento e itens por canal
SELECT * FROM vw_resumo_por_canal;


-- Desativa o modo de atualização segura
SET SQL_SAFE_UPDATES = 0;

-- Reativa o modo de atualização segura
SET SQL_SAFE_UPDATES = 1;