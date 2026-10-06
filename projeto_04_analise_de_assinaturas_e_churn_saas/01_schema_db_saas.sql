-- Criação do banco de dados e seleção de contexto
CREATE DATABASE IF NOT EXISTS db_saas_analytics;
USE db_saas_analytics;

-- 1. Tabela de Clientes (Dimensão)
CREATE TABLE IF NOT EXISTS tb_clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    pais VARCHAR(50) DEFAULT 'Brasil',
    data_cadastro DATETIME NOT NULL
);

-- 2. Tabela de Planos de Assinatura (Dimensão)
CREATE TABLE IF NOT EXISTS tb_planos (
    id_plano INT AUTO_INCREMENT PRIMARY KEY,
    nome_plano VARCHAR(50) NOT NULL,
    valor_mensal DECIMAL(10,2) NOT NULL,
    limite_usuarios INT NOT NULL
);

-- 3. Tabela de Assinaturas (Fato de Contratos)
CREATE TABLE IF NOT EXISTS tb_assinaturas (
    id_assinatura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_plano INT NOT NULL,
    data_inicio DATETIME NOT NULL,
    data_cancelamento DATETIME NULL,
    status_assinatura VARCHAR(20) NOT NULL, -- 'Ativo', 'Cancelado', 'Pendente'
    CONSTRAINT fk_assinatura_cliente FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente),
    CONSTRAINT fk_assinatura_plano FOREIGN KEY (id_plano) REFERENCES tb_planos(id_plano)
);

-- 4. Tabela de Histórico de Pagamentos (Fato Financeira)
CREATE TABLE IF NOT EXISTS tb_pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_assinatura INT NOT NULL,
    data_pagamento DATETIME NOT NULL,
    valor_pago DECIMAL(10,2) NOT NULL,
    status_pagamento VARCHAR(20) NOT NULL, -- 'Aprovado', 'Recusado', 'Estornado'
    CONSTRAINT fk_pagamento_assinatura FOREIGN KEY (id_assinatura) REFERENCES tb_assinaturas(id_assinatura)
);

SELECT * FROM tb_clientes;
SELECT * FROM tb_planos;
SELECT * FROM tb_assinaturas;
SELECT * FROM tb_pagamentos;