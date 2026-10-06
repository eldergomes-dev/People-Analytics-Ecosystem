# ==============================================================================
# PROJETO 04: Análise de Assinaturas e Churn SaaS
# ARQUIVO: 02_seed_saas.py
# DESCRIÇÃO: Povoamento ("Seed" / Inserção de Dados) em Python.
# FINALIDADE: Preencher os DataFrames com os dados simulados do projeto para
#             permitir o processamento das métricas SaaS.
# ==============================================================================

import pandas as pd

def gerar_dados_iniciais():
    """Gera e retorna as 4 tabelas do projeto preenchidas com os dados iniciais."""

    # 1. POVOAMENTO DA TABELA DE PLANOS (Dimensão de Ofertas)
    tb_planos = pd.DataFrame([
        {'id_plano': 1, 'nome_plano': 'Basic', 'valor_mensal': 49.90, 'limite_usuarios': 3},
        {'id_plano': 2, 'nome_plano': 'Pro', 'valor_mensal': 149.90, 'limite_usuarios': 10},
        {'id_plano': 3, 'nome_plano': 'Enterprise', 'valor_mensal': 499.90, 'limite_usuarios': 50}
    ])

    # 2. POVOAMENTO DA TABELA DE CLIENTES (Dimensão de Usuários)
    tb_clientes = pd.DataFrame([
        {'id_cliente': 1, 'nome': 'TechCorp Solucoes', 'email': 'contato@techcorp.com', 'pais': 'Brasil', 'data_cadastro': '2025-01-10 09:00:00'},
        {'id_cliente': 2, 'nome': 'Inovacao Digital LTDA', 'email': 'financeiro@inovacao.com', 'pais': 'Brasil', 'data_cadastro': '2025-01-15 14:30:00'},
        {'id_cliente': 3, 'nome': 'Global Soft Inc', 'email': 'admin@globalsoft.com', 'pais': 'Portugal', 'data_cadastro': '2025-02-01 11:15:00'},
        {'id_cliente': 4, 'nome': 'Alpha Analytics', 'email': 'suporte@alphaanalytics.com', 'pais': 'Brasil', 'data_cadastro': '2025-02-20 16:45:00'},
        {'id_cliente': 5, 'nome': 'Beta Logistics', 'email': 'operacoes@betalog.com', 'pais': 'Espanha', 'data_cadastro': '2025-03-05 10:00:00'}
    ])

    # 3. POVOAMENTO DA TABELA DE ASSINATURAS (Fato de Contratos)
    tb_assinaturas = pd.DataFrame([
        {'id_assinatura': 1, 'id_cliente': 1, 'id_plano': 2, 'data_inicio': '2025-01-10 09:30:00', 'data_cancelamento': None, 'status_assinatura': 'Ativo'},
        {'id_assinatura': 2, 'id_cliente': 2, 'id_plano': 1, 'data_inicio': '2025-01-15 15:00:00', 'data_cancelamento': '2025-04-15 10:00:00', 'status_assinatura': 'Cancelado'},
        {'id_assinatura': 3, 'id_cliente': 3, 'id_plano': 3, 'data_inicio': '2025-02-01 11:30:00', 'data_cancelamento': None, 'status_assinatura': 'Ativo'},
        {'id_assinatura': 4, 'id_cliente': 4, 'id_plano': 1, 'data_inicio': '2025-02-20 17:00:00', 'data_cancelamento': None, 'status_assinatura': 'Ativo'},
        {'id_assinatura': 5, 'id_cliente': 5, 'id_plano': 2, 'data_inicio': '2025-03-05 10:30:00', 'data_cancelamento': '2025-05-10 18:20:00', 'status_assinatura': 'Cancelado'}
    ])

    # 4. POVOAMENTO DA TABELA DE PAGAMENTOS (Fato Financeira)
    tb_pagamentos = pd.DataFrame([
        {'id_pagamento': 1, 'id_assinatura': 1, 'data_pagamento': '2025-01-10 09:35:00', 'valor_pago': 149.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 2, 'id_assinatura': 1, 'data_pagamento': '2025-02-10 09:00:00', 'valor_pago': 149.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 3, 'id_assinatura': 1, 'data_pagamento': '2025-03-10 09:00:00', 'valor_pago': 149.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 4, 'id_assinatura': 2, 'data_pagamento': '2025-01-15 15:05:00', 'valor_pago': 49.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 5, 'id_assinatura': 2, 'data_pagamento': '2025-02-15 09:00:00', 'valor_pago': 49.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 6, 'id_assinatura': 2, 'data_pagamento': '2025-03-15 09:00:00', 'valor_pago': 49.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 7, 'id_assinatura': 3, 'data_pagamento': '2025-02-01 11:35:00', 'valor_pago': 499.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 8, 'id_assinatura': 3, 'data_pagamento': '2025-03-01 09:00:00', 'valor_pago': 499.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 9, 'id_assinatura': 4, 'data_pagamento': '2025-02-20 17:05:00', 'valor_pago': 49.90, 'status_pagamento': 'Aprovado'},
        {'id_pagamento': 10, 'id_assinatura': 5, 'data_pagamento': '2025-03-05 10:35:00', 'valor_pago': 149.90, 'status_pagamento': 'Aprovado'}
    ])

    return tb_clientes, tb_planos, tb_assinaturas, tb_pagamentos

if __name__ == "__main__":
    tb_clientes, tb_planos, tb_assinaturas, tb_pagamentos = gerar_dados_iniciais()
    print("=== POVOAMENTO REALIZADO COM SUCESSO EM PYTHON ===")
    print(f"Total Clientes: {len(tb_clientes)} | Total Planos: {len(tb_planos)}")
    print(f"Total Assinaturas: {len(tb_assinaturas)} | Total Pagamentos: {len(tb_pagamentos)}")
