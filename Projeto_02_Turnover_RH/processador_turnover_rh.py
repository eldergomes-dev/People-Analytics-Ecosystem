import os
import pandas as pd
from datetime import datetime

# 1. Simulação dos dados brutos extraídos do Banco de Dados (SQL)
dados_colaboradores = [
    {"id_colaborador": 1, "nome": "Ana Silva", "departamento": "Tecnologia", "cargo": "Desenvolvedor Pleno", "salario": 7500.00, "data_admissao": "2023-01-15", "data_desligamento": None, "status": "Ativo", "tipo_desligamento": None, "motivo": None},
    {"id_colaborador": 2, "nome": "Carlos Souza", "departamento": "Tecnologia", "cargo": "Analista de Dados", "salario": 6200.00, "data_admissao": "2022-05-10", "data_desligamento": "2025-11-20", "status": "Desligado", "tipo_desligamento": "Voluntário", "motivo": "Proposta Salarial Maior"},
    {"id_colaborador": 3, "nome": "Mariana Lima", "departamento": "Vendas", "cargo": "Executivo de Contas", "salario": 5000.00, "data_admissao": "2024-02-01", "data_desligamento": "2025-08-14", "status": "Desligado", "tipo_desligamento": "Voluntário", "motivo": "Insatisfação com Metas"},
    {"id_colaborador": 4, "nome": "Roberto Alves", "departamento": "Vendas", "cargo": "Gerente de Contas", "salario": 9500.00, "data_admissao": "2021-03-20", "data_desligamento": None, "status": "Ativo", "tipo_desligamento": None, "motivo": None},
    {"id_colaborador": 5, "nome": "Fernanda Costa", "departamento": "RH", "cargo": "Business Partner", "salario": 6800.00, "data_admissao": "2022-11-01", "data_desligamento": "2026-01-10", "status": "Desligado", "tipo_desligamento": "Involuntário", "motivo": "Reestruturação de Área"},
    {"id_colaborador": 6, "nome": "Lucas Pereira", "departamento": "Tecnologia", "cargo": "Desenvolvedor Senior", "salario": 11000.00, "data_admissao": "2020-08-15", "data_desligamento": None, "status": "Ativo", "tipo_desligamento": None, "motivo": None},
    {"id_colaborador": 7, "nome": "Juliana Rocha", "departamento": "Marketing", "cargo": "Analista de Marketing", "salario": 4800.00, "data_admissao": "2023-06-01", "data_desligamento": "2025-12-05", "status": "Desligado", "tipo_desligamento": "Voluntário", "motivo": "Mudança de Carreira"},
    {"id_colaborador": 8, "nome": "Diego Martins", "departamento": "Financeiro", "cargo": "Analista Financeiro", "salario": 5500.00, "data_admissao": "2022-01-10", "data_desligamento": None, "status": "Ativo", "tipo_desligamento": None, "motivo": None},
    {"id_colaborador": 9, "nome": "Beatriz Mendes", "departamento": "Vendas", "cargo": "Executivo de Contas", "salario": 5200.00, "data_admissao": "2024-05-12", "data_desligamento": "2026-02-18", "status": "Desligado", "tipo_desligamento": "Voluntário", "motivo": "Proposta Salarial Maior"},
    {"id_colaborador": 10, "nome": "Thiago Melo", "departamento": "Tecnologia", "cargo": "DevOps Engineer", "salario": 8900.00, "data_admissao": "2023-09-01", "data_desligamento": None, "status": "Ativo", "tipo_desligamento": None, "motivo": None}
]

# 2. Carregar no DataFrame Pandas
df = pd.DataFrame(dados_colaboradores)

# 3. Tratamento de Datas e Cálculo do Tempo de Casa (Tenure em Meses)
df['data_admissao'] = pd.to_datetime(df['data_admissao'])
df['data_desligamento'] = pd.to_datetime(df['data_desligamento'])

hoje = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))

# Para ativos usa a data atual; para desligados usa a data de desligamento
df['data_fim'] = df["data_desligamento"].fillna(hoje)
df['tenure_meses'] = round((df['data_fim'] - df['data_admissao']).dt.days / 30.44, 1)

# Categorização do Tempo de Casa
def categorizar_tenure(meses):
    if meses <= 12:
        return 'Até 1 ano'
    elif meses <= 24:
        return '1 a 2 anos'
    elif meses <= 36:
        return '2 a 3 anos'
    else:
        return 'Mais de 3 anos'

df['faixa_tenure'] = df['tenure_meses'].apply(categorizar_tenure)

# Preenchimento de nulos para exportação limpa
df['tipo_desligamento'] = df['tipo_desligamento'].fillna('N/A')
df['motivo'] = df['motivo'].fillna('N/A')
df.drop(columns=['data_fim'], inplace=True)

# 4. Exportação para CSV (Garante salvamento SEMPRE na mesma pasta deste script)
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_script, 'base_intermediaria_turnover.csv')

df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')

print(f"Processamento concluído com sucesso!")
print(f"Arquivo gerado em: {caminho_csv}")
print("\n--- Resumo dos Dados Tratados ---")
print(df[['nome', 'departamento', 'status', 'tenure_meses', 'faixa_tenure']])