import sqlite3

print('Etapa 2: Inserindo dados nas tabelas dimensão e fato...')

conexao_banco_dados = sqlite3.connect('banco_ecommerce.db')
cursor_banco_dados = conexao_banco_dados.cursor()

# 1. inserindo Clientes
lista_clientes = [
    ('Elder gomes', 'São Paulo', 'SP', 'Corporativo'),
    ('Ana Silva', 'Rio de Janeiro', 'RJ', 'Varejo'),
    ('Carlos Oliveira', 'Belo Horizonte', 'MG', 'Varejo'),
    ('Mariana Santos', 'Curitiba', 'PR', 'Corporativo'),
    ('Roberto Souza', 'Porto Alegre', 'RS', 'Varejo')
]

cursor_banco_dados.executemany('''
    INSERT INTO dim_clientes (nome_cliente, cidade, estado, segmento)
    VALUES (?, ?, ?, ?);
''', lista_clientes)

# 2. Inserindo Produtos
lista_produtos = [
    ('Teclado Mecânico RGB', 'Periféricos', 250.00),
    ('Mouse Sem Fio Ergônomico', 'Periféricos', 120.00),
    ('Monitor 27 Polegadas 4K', 'Monitores', 1800.00),
    ('Cadeira Ergonômica', 'Móveis', 950.00),
    ('Headset Gamer 7.1', 'Áudio', 350.00)
]

cursor_banco_dados.executemany('''
    INSERT INTO dim_produtos (nome_produto, categoria, preco_tabela)
    VALUES (?, ?, ?);
''', lista_produtos)

# 3. Inserindo Canais de Venda
lista_canais = [
    ('Website',),
    ('Aplicativo Mobile',),
    ('Loja Física',),
    ('Marketplace',)
]

cursor_banco_dados.executemany('''
    INSERT INTO dim_canais (nome_canal)
    VALUES (?);
''', lista_canais)

# 4. Inserindo Fato Vendas
lista_fato_vendas = [
    ('2026-08-01', 1, 3, 1, 1, 1800.00, 100.00),
    ('2026-08-02', 2, 1, 2, 2, 250.00, 20.00),
    ('2026-08-03', 3, 4, 3, 1, 950.00, 50.00),
    ('2026-08-04', 4, 2, 4, 3, 120.00, 0.00),
    ('2026-08-05', 5, 5, 1, 1, 350.00, 15.00),
    ('2026-08-06', 1, 1, 2, 1, 250.00, 0.00),
    ('2026-08-07', 2, 3, 1, 1, 1800.00, 150.00),
    ('2026-08-08', 3, 5, 4, 2, 350.00, 30.00)
]

cursor_banco_dados.executemany('''
INSERT INTO fato_vendas (data_venda, id_cliente, id_produto, id_canal, quantidade, valor_unitario, valor_desconto)
VALUES (?, ?, ?, ?, ?, ?, ?);
''', lista_fato_vendas)

conexao_banco_dados.commit()
conexao_banco_dados.close()

print('Etapa 2 concluída: Dados inseridos com sucesso nas tabelas dimensão e fato.')