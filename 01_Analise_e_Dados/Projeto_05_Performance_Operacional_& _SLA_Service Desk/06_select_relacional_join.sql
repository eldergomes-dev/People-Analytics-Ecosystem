/*
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 06_select_relacional_join.sql
===============================================================================

1. PARA QUE SERVE ESTE CÓDIGO?
   Este código realiza uma consulta relacional (JOIN) entre a tabela principal 
   (Fato_Chamados) e as tabelas de apoio (Dimensão_Atendentes e Dimensão_Categorias). 
   Ele unifica dados espalhados em uma única visão tabular e amigável para leitura.

2. ONDE E COMO POSSO USAR?
   - ONDE: MySQL Workbench, DBeaver, VS Code, Scripts Python, Power BI (via SQL nativo) 
     ou qualquer ferramenta de conexão a banco de dados MySQL.
   - COMO: Copie e execute o comando dentro do seu SGBD (Sistema Gerenciador de Banco 
     de Dados) com a base 'db_service_desk' selecionada.

3. PROGRAMAS ONDE ESTE CÓDIGO SERÁ INTEGRADO:
   - MySQL Workbench: Validação visual e testes da consulta.
   - Python (VS Code): Ingestão direta dos dados consolidados usando pandas/SQLAlchemy.
   - Power BI: Importação limpa dos dados via query SQL para montagem do Star Schema.

4. OBJETIVO DO CÓDIGO:
   Eliminar a necessidade de visualizar apenas IDs numéricos (ex: id_atendente = 1) 
   e trazer os nomes reais, níveis de suporte, categorias e SLAs de atendimento, 
   permitindo analisar a performance e o cumprimento de metas de forma clara.
===============================================================================
*/


SELECT 
    fato_chamados.id_chamado,
    dimensao_atendentes.nome_atendente,
    dimensao_atendentes.nivel_atendimento,
    dimensao_categorias.nome_categoria,
    dimensao_categorias.sla_horas_limite,
    fato_chamados.tempo_resolucao_horas,
    fato_chamados.status_chamado,
    fato_chamados.cumpre_sla
FROM fato_chamados
INNER JOIN dimensao_atendentes ON fato_chamados.id_atendente = dimensao_atendentes.id_atendente
INNER JOIN dimensao_categorias ON fato_chamados.id_categoria = dimensao_categorias.id_categoria;