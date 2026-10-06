# aula.py
# Modulo em linguagem Python para ler os dados do banco MySQL,
# calcular o indicador de absenteismo e exportar o resultado limpo.

import pandas as pandas_lib

def processar_metricas_colaboradores():
    # Representacao dos dados extraidos da tabela do MySQL
    dados_banco_mysql = [
        {
            "nome_completo": "Elder Gomes",
            "departamento": "TI",
            "cargo": "Analista de People Analytics",
            "salario_base": 5500.00,
            "dias_trabalhados": 20,
            "dias_faltas": 1,
        },
        {
            "nome_completo": "Maria Silva",
            "departamento": "Recursos humanos",
            "cargo": "Especialista de R&S",
            "salario_base": 4800.00,
            "dias_trabalhados": 22,
            "dias_faltas": 0,
        },
        {
            "nome_completo": "Carlos Souza",
            "departamento": "Operações",
            "cargo": "Assistente Administração",
            "salario_base": 3200.00,
            "dias_trabalhados": 18,
            "dias_faltas": 4,
        }
    ]

    # Convertendo a lista de dados em uma estrutura de tabela na memoria
    tabela_dados = pandas_lib.DataFrame(dados_banco_mysql)

    # Calculando a taxa percentual de absenteismo
    tabela_dados['dias_totais'] = tabela_dados['dias_trabalhados'] + tabela_dados['dias_faltas']
    tabela_dados['percentual_taxa_absenteismo'] = (tabela_dados['dias_faltas'] / tabela_dados['dias_totais']) * 100
    tabela_dados['percentual_taxa_absenteismo'] = tabela_dados['percentual_taxa_absenteismo'].round(2)

    # Salva o arquivo Comma-Separated Values (Valores Separados por Virgula) na pasta do projeto
    tabela_dados.to_csv('indicador_absenteismo.csv', index=False, sep=';', encoding='utf-8-sig')
    
    print("Processamento do Projeto 01 concluído com sucesso!")
    print("O arquivo 'indicador_absenteismo.csv' foi gerado na pasta do projeto.")

# Bloco de execucao principal (ficou fora da funcao, alinhado a esquerda)
if __name__ == "__main__":
    processar_metricas_colaboradores()