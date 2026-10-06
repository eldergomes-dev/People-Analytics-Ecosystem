-- ============================================================
-- PROJETO 03: VENDAS E-COMMERCE MULTICANAL
-- ARQUIVO: 01_criar_tabelas_ecommerce.sql
-- OBJETIVO: Criar o banco de dados e as tabelas (Star Schema - esquema em estrela)
-- ============================================================

-- 1. Criação do Banco de Dados com suporte a acentuação
CREATE DATABASE IF NOT EXISTS banco_ecommerce
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_unicode_ci;

-- Seleciona o banco de dados para execução dos comandos
USE banco_ecommerce;

-- ============================================================
-- TABELAS DIMENSÃO (CADASTROS)
-- ============================================================

-- 2. Tabela Dimensão: Clientes
CREATE TABLE dim_clientes(
	id_cliente INT AUTO_INCREMENT PRIMARY KEY, -- Chave Primária
    nome_cliente VARCHAR(100) NOT NULL,			-- Nome completo do Cliente	
    cidade VARCHAR(50),							-- Cidade de Residência
    estado CHAR(2),								-- Sigla do Estado (ex: RJ, SP)
    segmento VARCHAR(30)						-- Categoria de Cliente (ex: Varejo, Corporativo)
);

-- 3. Tabela Dimensão: Produtos
CREATE TABLE dim_produtos (
	id_produto INT AUTO_INCREMENT PRIMARY KEY, -- Chave primária
    nome_produto VARCHAR(100) NOT NULL,			-- Nome do Item
    categoria VARCHAR(50),						-- Categoria do Produto
    preco_tabela DECIMAL(10, 2) NOT NULL		-- Valor de Tabela
);

-- 4. Tabela Dimensão: Canais de Venda
CREATE TABLE dim_canais (
	id_canal INT AUTO_INCREMENT PRIMARY KEY,	-- Chave Primária
    nome_canal VARCHAR(50) NOT NULL				-- Meio de venda (ex: Site, App, Loja)
);

-- ============================================================
-- TABELA FATO (REGISTRO DE TRANSAÇÕES)
-- ============================================================

-- 5: Tabela Fato: Vendas
CREATE TABLE fato_vendas (
	id_venda INT AUTO_INCREMENT PRIMARY KEY,	-- Chave Primária da Transação
    data_venda DATE NOT NULL,					-- Data da Operação
    id_cliente INT NOT NULL,					-- Chave Estrangeira -> Clientes
    id_produto INT NOT NULL,					-- Chave Estrangeira -> Produtos
    id_canal INT NOT NULL,						-- Chave Estrangeira -> Canais
    quantidade INT NOT NULL, 					-- Volume de Itens Vendidos
    valor_unitario DECIMAL(10, 2) NOT NULL,		-- Preço Aplicado na Venda
    valor_desconto DECIMAL(10, 2) DEFAULT 0.00,	-- Abatimento Aplicado

-- Relacionamentos (Integridade Referencial)
CONSTRAINT fk_vendas_clientes FOREIGN KEY (id_cliente) REFERENCES dim_clientes(id_cliente),
CONSTRAINT fk_vendas_produtos FOREIGN KEY (id_produto) REFERENCES dim_produtos(id_produto),
CONSTRAINT fk_vendas_canais FOREIGN KEY (id_canal) REFERENCES dim_canais(id_canal)

);



-- Desativa o modo de atualização segura para permitir UPDATE na tabela inteira
SET SQL_SAFE_UPDATES = 0;

-- Reativa o modo de atualização segura
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM dim_clientes;
SELECT * FROM dim_produtos;
SELECT * FROM dim_canais;
SELECT * FROM fato_vendas;