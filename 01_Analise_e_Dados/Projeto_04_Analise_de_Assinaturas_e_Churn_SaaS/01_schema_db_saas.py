# ==============================================================================
# PROJETO 04: Análise de Assinaturas e Churn SaaS
# ARQUIVO: 01_schema_saas.py
# DESCRIÇÃO: Criação da Estrutura de Dados (Schema) em Python.
# FINALIDADE: Definir as colunas e tipos de dados para as 4 tabelas do projeto
#             usando Pandas DataFrames (sem dados/registros).
# ==============================================================================

from unicodedata import name

import pandas as pd     

# 1. Definição do Schema da Tabela de Clientes (Dimensão)
tb_clientes_schema = pd.DataFrame(columns=[
    'id_cliente',
    'nome',
    'email',
    'pais',
    'data_cadastro'
])

# 2. Definição do Schema da Tabela de Planos (Dimensão)
tb_planos_schema = pd.DataFrame(columns=[
    'id_plano',
    'nome_plano',
    'valor_mensal',
    'limite_usuarios'
])

# 3. Definição do Schema da Tabela de Assinaturas (Fato de Contratos)
tb_assinaturas_schema = pd.DataFrame(columns=[
    'id_assinatura',
    'id_cliente',
    'id_plano',
    'data_cancelamento',
    'status_assinatura'
])

# 4. Definição do Schema da Tabela de Pagamentos (Fato Financeira)
tb_pagamentos_schema = pd.DataFrame(columns=[
    'id_pagamento',
    'id_assinatura',
    'data_pagamento',
    'valor_pago',
    'status_pagamento'
])

# Validação das estruturas criadas
if __name__ == "__main__":
    print("=== SCHEMAS CRIADOS COM SUCESSO NO PYTHON ===")
    print("\n[tb_clientes]:", list(tb_clientes_schema.columns))
    print("[tb_planos]:", list(tb_planos_schema.columns))
    print("[tb_assinaturas]:", list(tb_assinaturas_schema.columns))
    print("[tb_pagamentos]:", list(tb_pagamentos_schema.columns))
