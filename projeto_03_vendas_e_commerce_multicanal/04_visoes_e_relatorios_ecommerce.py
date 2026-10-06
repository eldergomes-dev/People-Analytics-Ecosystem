import sqlite3
import pandas 

print('Etapa 4: Criando visões (Views) e exportando o arquivo de valores separados por vírgula (CSV)...')

conexao_banco_dados = sqlite3.connect('banco_ecommerce.db')
cursor_banco_dados = conexao_banco_dados.cursor()

# 1. Criação da Visão Consolidada de Vendas
cursor_banco_dados.execute('''
CREATE VIEW IF NOT EXISTS vw_vendas_consolidadas AS
SELECT 
    fato_vendas.id_venda,
    fato_vendas.data_venda,
    dim_clientes.nome_cliente,
    dim_clientes.cidade AS cidade_cliente,
    dim_clientes.estado AS estado_cliente,
    dim_clientes.segmento AS segmento_cliente, 
    dim_produtos.nome_produto,
    dim_produtos.categoria AS categoria_produto,
    dim_canais.nome_canal,
    fato_vendas.quantidade,
    fato_vendas.valor_unitario,
    fato_vendas.valor_desconto,
    fato_vendas.valor_total_bruto,
    fato_vendas.valor_total_liquido,
    fato_vendas.status_venda
FROM fato_vendas
INNER JOIN dim_clientes 
    ON fato_vendas.id_cliente = dim_clientes.id_cliente
INNER JOIN dim_produtos 
    ON fato_vendas.id_produto = dim_produtos.id_produto
INNER JOIN dim_canais 
    ON fato_vendas.id_canal = dim_canais.id_canal;
''')

# 2. Criação da Visão de Resumo por Canal de Venda
cursor_banco_dados.execute('''
CREATE VIEW IF NOT EXISTS vw_resumo_por_canal AS
SELECT 
    dim_canais.nome_canal,
    COUNT(fato_vendas.id_venda) AS total_pedidos,
    SUM(fato_vendas.quantidade) AS quantidade_total_itens,
    SUM(fato_vendas.valor_total_liquido) AS faturamento_total_liquido
FROM fato_vendas
INNER JOIN dim_canais 
    ON fato_vendas.id_canal = dim_canais.id_canal
GROUP BY dim_canais.nome_canal;
''')

conexao_banco_dados.commit()

# 3. Extraindo a visão consolidada com pandas e gerando o CSV final
consulta_linguagem_consulta_estruturada = 'SELECT * FROM vw_vendas_consolidadas;'
quadro_de_dados = pandas.read_sql_query(consulta_linguagem_consulta_estruturada, conexao_banco_dados)

caminho_arquivo_saida = 'vw_vendas_consolidadas.csv'
quadro_de_dados.to_csv(caminho_arquivo_saida, index=False, encoding='utf-8-sig')

conexao_banco_dados.close()

print(f'Sucesso: Views criadas e relatório \'{caminho_arquivo_saida}\' exportado com {len(quadro_de_dados)} linhas!')