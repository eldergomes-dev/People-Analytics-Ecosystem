# ==============================================================================
# PROJETO 04: Análise de Assinaturas e Churn SaaS
# ARQUIVO: 04_relatorio_final_saas.py
# DESCRIÇÃO: Consolidação, Geração de Base Analítica e Exportação CSV Otimizada.
# FINALIDADE: Cruzar tabelas e exportar CSVs limpos com separador de ponto e vírgula
#             e vírgula decimal para integração perfeita no Google Planilhas (PT-BR).
# ESTILO: Nomes literais e descritivos em todas as variáveis e DataFrames.
# ==============================================================================

import os
import importlib
import pandas as pd

# Carregamento do módulo '02_seed_saas'
seed_saas = importlib.import_module("02_seed_saas")
tb_clientes, tb_planos, tb_assinaturas, tb_pagamentos = seed_saas.gerar_dados_iniciais()

# Carregamento do módulo '03_queries_churn_saas'
queries_saas = importlib.import_module("03_queries_churn_saas")
relatorio_por_plano = queries_saas.relatorio_por_plano
relatorio_ltv_clientes = queries_saas.relatorio_ltv_clientes
receita_recorrente_mensal_mrr = queries_saas.receita_recorrente_mensal_mrr
taxa_churn_percentual = queries_saas.taxa_churn_percentual
receita_media_por_usuario_arpu = queries_saas.receita_media_por_usuario_arpu
total_assinantes_ativos = queries_saas.total_assinantes_ativos
total_cancelamentos_churn = queries_saas.total_cancelamentos_churn


# 1. CONSTRUÇÃO DA BASE ANALÍTICA CONSOLIDADA (DATASET PARA PLANILHAS / POWER BI)
tb_base_analitica_saas = pd.merge(tb_pagamentos, tb_assinaturas, on='id_assinatura', how='left')
tb_base_analitica_saas = pd.merge(tb_base_analitica_saas, tb_clientes, on='id_cliente', how='left')
tb_base_analitica_saas = pd.merge(tb_base_analitica_saas, tb_planos, on='id_plano', how='left')

# Seleção e renomeação exata das colunas da base analítica
tb_base_analitica_saas = tb_base_analitica_saas[[
    'id_pagamento',
    'id_assinatura',
    'id_cliente',
    'nome',
    'email',
    'id_plano',
    'nome_plano',
    'valor_mensal',
    'status_assinatura',
    'data_inicio',
    'data_cancelamento',
    'data_pagamento',
    'valor_pago',
    'status_pagamento'
]].rename(columns={
    'nome': 'nome_cliente',
    'valor_mensal': 'valor_mensal_plano',
    'data_inicio': 'data_inicio_assinatura'
})


# 2. QUADRO RESUMO DE MÉTRICAS EXECUTIVAS (APENAS 2 COLUNAS: INDICADOR E VALOR)
tb_resumo_executivo_saas = pd.DataFrame([
    {"indicador": "Receita Recorrente Mensal (MRR)", "valor": round(receita_recorrente_mensal_mrr, 2)},
    {"indicador": "Total de Assinantes Ativos", "valor": int(total_assinantes_ativos)},
    {"indicador": "Receita Média Por Usuário (ARPU)", "valor": round(receita_media_por_usuario_arpu, 2)},
    {"indicador": "Taxa de Churn", "valor": round(taxa_churn_percentual / 100, 4)},
    {"indicador": "Total de Cancelamentos Históricos", "valor": int(total_cancelamentos_churn)}
])


# 3. EXPORTAÇÃO DOS ARQUIVOS CSV NO PADRÃO PT-BR (PONTO E VÍRGULA E VÍRGULA DECIMAL)
diretorio_saida = "relatorios_saida"
if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)

caminho_csv_base_analitica = os.path.join(diretorio_saida, "base_analitica_saas_powerbi.csv")
caminho_csv_resumo = os.path.join(diretorio_saida, "01_resumo_executivo_saas.csv")
caminho_csv_planos = os.path.join(diretorio_saida, "02_desempenho_por_plano.csv")
caminho_csv_ltv = os.path.join(diretorio_saida, "03_ltv_por_cliente.csv")

# Exportando todos os arquivos configurados com sep=";" e decimal=","
tb_base_analitica_saas.to_csv(caminho_csv_base_analitica, index=False, sep=";", decimal=",", encoding="utf-8-sig")
tb_resumo_executivo_saas.to_csv(caminho_csv_resumo, index=False, sep=";", decimal=",", encoding="utf-8-sig")
relatorio_por_plano.to_csv(caminho_csv_planos, index=False, sep=";", decimal=",", encoding="utf-8-sig")
relatorio_ltv_clientes.to_csv(caminho_csv_ltv, index=False, sep=";", decimal=",", encoding="utf-8-sig")


# IMPRESSÃO DE CONFIRMAÇÃO NO TERMINAL
if __name__ == "__main__":
    print("=" * 70)
    print("GERAÇÃO DE RELATÓRIOS SAAS CONCLUÍDA")
    print("=" * 70)
    print("\nRESUMO EXECUTIVO (DADOS EXPORTADOS):")
    print(tb_resumo_executivo_saas.to_string(index=False))
    
    print("\n" + "=" * 70)
    print(f"ARQUIVOS CSV ATUALIZADOS NA PASTA '{diretorio_saida}':")
    print(f" -> {caminho_csv_resumo}")
    print(f" -> {caminho_csv_planos}")
    print(f" -> {caminho_csv_ltv}")
    print(f" -> {caminho_csv_base_analitica}")
    print("=" * 70)