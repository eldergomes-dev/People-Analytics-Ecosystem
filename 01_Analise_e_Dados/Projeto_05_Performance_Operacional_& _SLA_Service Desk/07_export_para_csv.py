"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 07_export_para_csv.py

1. PARA QUE SERVE ESTE CÓDIGO?
   Este código conecta ao banco SQLite, executa a consulta relacional (JOIN)
   e exporta o resultado consolidado em formato CSV.

2. ONDE E COMO POSSO USAR OS DADOS GERADOS?
   - Google Planilhas: Importação direta do arquivo 'relatorio_service_desk.csv'.
   - Power BI: Fonte de dados de texto/CSV para criação de dashboards.
   - Excel: Abertura direta sem erros de acentuação ou desalinhamento de colunas.

3. EXPLICAÇÃO TÉCNICA DAS CONFIGURAÇÕES DO CSV:
   - encoding='utf-8-sig': Inclui a marca de ordem de byte (BOM), garantindo 
     que caracteres com acento (ex: 'NÍVEL', 'Não') sejam lidos corretamente.
   - delimiter=';': Utiliza ponto e vírgula para que o Excel e Power BI façam 
     a separação automática das colunas em sistemas com padrão de linguagem PT-BR.
===============================================================================
"""

import sqlite3
import csv

# -- 1. Conexão ao banco de dados SQLite --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- 2. Consulta Relacional (INNER JOIN) trazendo os dados consolidados --
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

# -- 3. Definição dos nomes das colunas (Cabeçalho do relatório) --
cabecalho = [
    "ID_Chamado",
    "Atendente",
    "Nivel_Atendimento",
    "Categoria",
    "SLA_Horas_Limite",
    "Tempo_Resolucao_Horas",
    "Status_Chamado",
    "Cumpre_SLA"
]

# -- 4. Nome do arquivo CSV de saída --
nome_arquivo = "relatorio_service_desk.csv"

# -- 5. Criação e escrita do arquivo CSV --
# newline="" evita linhas em branco extras entre os registros
with open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";")
    
    # Escreve a primeira linha com o nome dos cabeçalhos
    escritor.writerow(cabecalho)
    
    # Escreve todas as linhas de dados retornadas pela consulta SQL
    escritor.writerows(resultados)

print("=" * 60)
print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado.")
print("Pronto para importação no Power BI e Google Planilhas.")
print("=" * 60)

# -- 6. Fechamento da conexão com o banco de dados --
conexao.close()