"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 06_select_relacional_join.py

1. PARA QUE SERVE ESTE CÓDIGO?
   Este código realiza uma consulta relacional (JOIN) entre a tabela principal 
   (fato_chamados) e as tabelas de apoio (dimensao_atendentes e dimensao_categorias). 
   Ele unifica dados espalhados em uma única visão tabular e amigável para leitura.

2. ONDE E COMO POSSO USAR?
   - ONDE: VS Code, Terminal CMD/PowerShell ou integrado em pipelines Python.
   - COMO: Execute via terminal com 'py 06_select_relacional_join.py'.

3. PROGRAMAS ONDE ESTE CÓDIGO SERÁ INTEGRADO:
   - Python (VS Code): Execução da consulta relacional via sqlite3.
   - Power BI / Pandas: Ingestão direta dos dados para geração de relatórios.

4. OBJETIVO DO CÓDIGO:
   Eliminar a necessidade de visualizar apenas IDs numéricos (ex: id_atendente = 1) 
   e trazer os nomes reais, níveis de suporte, categorias e SLAs de atendimento, 
   permitindo analisar a performance e o cumprimento de metas de forma clara.
===============================================================================
"""

import sqlite3

# -- 1. Conexão ao banco de dados --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- 2. Consulta Relacional (INNER JOIN) mantendo nomes completos das tabelas --
query_relacional = """
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
"""

cursor.execute(query_relacional)
resultados = cursor.fetchall()

# -- 3. Exibição dos dados consolidados no terminal --
# -- Formatação do Cabeçalho da Tabela no Terminal --
# O modificador :<X alinha o texto à esquerda e reserva exatamente X caracteres de largura.
# Isso garante que os nomes das colunas fiquem perfeitamente alinhados com os dados das linhas abaixo.
print("\n" + "="*95)
print(f"{'ID':<5} | {'ATENDENTE':<16} | {'NÍVEL':<6} | {'CATEGORIA':<24} | {'SLA(h)':<6} | {'TEMPO(h)':<8} | {'STATUS':<10} | {'SLA OK?'}")
print("="*95)


# -- Iteração pelos resultados: desempacota a tupla e formata os valores para exibição limpa no terminal --
for linha in resultados:
    id_chamado, atendente, nivel, categoria, sla, tempo, status, cumpre = linha
    tempo_str = f"{tempo:.2f}" if tempo is not None else "N/A"
    print(f"{id_chamado:<5} | {atendente:<16} | {nivel:<6} | {categoria:<24} | {sla:<6} | {tempo_str:<8} | {status:<10} | {cumpre}")

print("="*95 + "\n")

# Fecha a conexão
conexao.close()