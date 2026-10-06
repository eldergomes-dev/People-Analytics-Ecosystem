import sqlite3

print('Etapa 1: Criando banco de dados e tabelas...')
conexao_banco_dados = sqlite3.connect('banco_ecommerce.db')
cursor_banco_dados = conexao_banco_dados.cursor()

# 1. Tabela Dimensão: Clientes
cursor_banco_dados.execute('''
CREATE TABLE IF NOT EXISTS dim_clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    cidade TEXT,
    estado TEXT,
    segmento TEXT
);
''')

# 2. Tabela Fato: Produtos
cursor_banco_dados.execute('''
CREATE TABLE IF NOT EXISTS dim_produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    categoria TEXT,
    preco_tabela REAL NOT NULL
);
''')    

# 3. Tabela Dimensão: Canais de Venda
cursor_banco_dados.execute('''
CREATE TABLE IF NOT EXISTS dim_canais (
    id_canal INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_canal TEXT NOT NULL
);
''')

# 4. Tabela Fato: Vendas
cursor_banco_dados.execute('''
CREATE TABLE IF NOT EXISTS fato_vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda TEXT NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    id_canal INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    valor_desconto REAL DEFAULT 0.00,
    FOREIGN KEY (id_cliente) REFERENCES dim_clientes (id_cliente),
    FOREIGN KEY (id_produto) REFERENCES dim_produtos (id_produto),
    FOREIGN KEY (id_canal) REFERENCES dim_canais (id_canal)
);
''')

conexao_banco_dados.commit()
conexao_banco_dados.close()

print('Etapa 1 concluída: Banco de dados e tabelas criados com sucesso.')


