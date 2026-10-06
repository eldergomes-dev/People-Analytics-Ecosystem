-- ============================================================================
-- PROJETO: People Analytics - Módulo de Banco de Dados de RH
-- ARQUIVO: estrutura_e_metricas_rh.sql
-- OBJETIVO: Criar a tabela de colaboradores e consultar a taxa de absenteísmo.
-- ============================================================================

-- 1. Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS rh_analytics;
USE rh_analytics; 

-- 2. Criação da Tabela de Colaboradores
CREATE TABLE IF NOT EXISTS colaboradores(
	id_colaborador INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario_base DECIMAL(10, 2) NOT NULL,
    dias_trabalhados INT NOT NULL,
    dias_faltas INT NOT NULL,
    status_ativo BOOLEAN DEFAULT TRUE,
    data_admissao DATE NOT NULL
);

-- 3. Inserção de Dados para Teste
INSERT INTO colaboradores (
	nome_completo,
    departamento,
    cargo,
    salario_base,
    dias_trabalhados,
    dias_faltas,
    status_ativo,
	data_admissao 
)
VALUES
('Elder Gomes', 'TI', 'Analista de People Analytics', 5500.00, 20, 1, TRUE, '2024-01-15'),
('Maria Silva', 'Recursos humanos', 'Especialista de R&S', 4800.00, 22, 0, TRUE, '2023-06-10'),
('Carlos Souza', 'Operações', 'Assistente Administração', 3200.00, 18, 4, TRUE, '2024-03-01');

-- 4. Consulta de Indicadores de Absenteísmo
SELECT 
	nome_completo,
    departamento,
    dias_trabalhados,
    dias_faltas,
    ROUND((dias_faltas / (dias_trabalhados + dias_faltas)) * 100, 2) AS percentual_taxa_absenteismo,
    CASE
		WHEN (dias_faltas / (dias_trabalhados + dias_faltas)) * 100 > 5.0 THEN 'Alerta: Absenteismo alto'
        ELSE 'Normal'
	END AS status_assiduidade
FROM colaboradores;
	

