# ==============================================================================
# PROJETO 04: Análise de Assinaturas e Churn SaaS
# ARQUIVO: 03_queries_churn_saas.py
# DESCRIÇÃO: Consultas de Negócio e Métricas SaaS (MRR, Churn, ARPU, LTV) em Python.
# FINALIDADE: Realizar os cruzamentos de dados (equivalente aos JOINs) e calcular
#             os indicadores-chave de desempenho usando a biblioteca Pandas.
# ESTILO: Nomes literais e descritivos em todas as variáveis e DataFrames.
# ==============================================================================

import pandas as pd
import importlib

# Carregamento do módulo '02_seed_saas' utilizando importlib devido ao nome iniciar com número
seed_saas = importlib.import_module("02_seed_saas")
gerar_dados_iniciais = seed_saas.gerar_dados_iniciais

# Carregamento dos dados criados no arquivo 02_seed_saas.py
tb_clientes, tb_planos, tb_assinaturas, tb_pagamentos = gerar_dados_iniciais()

# 1. RECEITA RECORRENTE MENSAL (MRR - Monthly Recurring Revenue)
# Unindo a Tabela de Assinaturas com a Tabela de Planos pelo campo 'id_plano'
tb_assinaturas_com_planos = pd.merge(
    tb_assinaturas,
    tb_planos,
    on='id_plano',
    how='inner'
)

# Filtrando apenas as assinaturas com status 'Ativo'
tb_assinaturas_ativas = tb_assinaturas_com_planos[
    tb_assinaturas_com_planos['status_assinatura'] == 'Ativo'
]

receita_recorrente_mensal_mrr = tb_assinaturas_ativas['valor_mensal'].sum()
total_assinantes_ativos = len(tb_assinaturas_ativas)


# 2. TAXA DE CANCELAMENTO DE CLIENTES (Churn Rate %)
total_cancelamentos_churn = len(
    tb_assinaturas[tb_assinaturas['status_assinatura'] == 'Cancelado']
)
total_clientes_historico = len(tb_assinaturas)

taxa_churn_percentual = round(
    (total_cancelamentos_churn / total_clientes_historico) * 100, 2
)


# 3. RECEITA MÉDIA POR USUÁRIO (ARPU - Average Revenue Per User)
receita_media_por_usuario_arpu = round(
    receita_recorrente_mensal_mrr / total_assinantes_ativos, 2
)


# 4. DISTRIBUIÇÃO DE RECEITA E CANCELAMENTOS POR TIPO DE PLANO
tb_desempenho_planos = pd.merge(
    tb_planos,
    tb_assinaturas,
    on='id_plano',
    how='left'
)

# Agrupando por plano e calculando as métricas por categoria
relatorio_por_plano = tb_desempenho_planos.groupby(['id_plano', 'nome_plano']).agg(
    total_contratos_historico=('id_assinatura', 'count'),
    receita_mensal_por_plano=('valor_mensal', lambda valores: valores[tb_desempenho_planos.loc[valores.index, 'status_assinatura'] == 'Ativo'].sum()),
    total_cancelamentos_por_plano=('status_assinatura', lambda status: (status == 'Cancelado').sum())
).reset_index()


# 5. LIFETIME VALUE (LTV - Valor Total Gerado por Cliente)
# Cruzando Pagamentos -> Assinaturas -> Clientes -> Planos
tb_pagamentos_assinaturas = pd.merge(tb_pagamentos, tb_assinaturas, on='id_assinatura')
tb_completa_clientes = pd.merge(tb_pagamentos_assinaturas, tb_clientes, on='id_cliente')
tb_completa_clientes = pd.merge(tb_completa_clientes, tb_planos, on='id_plano')

# Filtrando apenas pagamentos aprovados
tb_pagamentos_aprovados = tb_completa_clientes[
    tb_completa_clientes['status_pagamento'] == 'Aprovado'
]

relatorio_ltv_clientes = tb_pagamentos_aprovados.groupby(
    ['id_cliente', 'nome', 'nome_plano']
)['valor_pago'].sum().reset_index()

relatorio_ltv_clientes.rename(
    columns={'nome': 'nome_cliente', 'valor_pago': 'valor_total_historico_ltv'},
    inplace=True
)

# IMPRESSÃO DOS RESULTADOS DAS CONSULTAS NO TERMINAL
if __name__ == "__main__":
    print("=" * 70)
    print("CONSULTAS DE MÉTRICAS SAAS - PROCESSADAS EM PYTHON")
    print("=" * 70)
    print(f"1. MRR Total: R$ {receita_recorrente_mensal_mrr:.2f} | Ativos: {total_assinantes_ativos}")
    print(f"2. Taxa de Churn: {taxa_churn_percentual}% | Total Cancelados: {total_cancelamentos_churn}")
    print(f"3. ARPU (Receita Média por Usuário): R$ {receita_media_por_usuario_arpu:.2f}")
    print("-" * 70)
    print("\n4. DESEMPENHO POR PLANO:")
    print(relatorio_por_plano.to_string(index=False))
    print("-" * 70)
    print("\n5. LIFETIME VALUE (LTV) POR CLIENTE:")
    print(relatorio_ltv_clientes.to_string(index=False))