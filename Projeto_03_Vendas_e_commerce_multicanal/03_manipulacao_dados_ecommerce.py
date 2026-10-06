import sqlite3

print('Etapa 3: Evoluindo a tabela fato com novas colunas e regras de negócio...')

conexao_banco_dados = sqlite3.connect('banco_ecommerce.db')
cursor_banco_dados = conexao_banco_dados.cursor()

# 1. Adicionando novas colunas na tabela fato
try:
    cursor_banco_dados.execute('ALTER TABLE fato_vendas ADD COLUMN valor_total_bruto REAL;')
    cursor_banco_dados.execute('ALTER TABLE fato_vendas ADD COLUMN valor_total_liquido REAL;')
    cursor_banco_dados.execute('ALTER TABLE fato_vendas ADD COLUMN status_venda TEXT;')
except sqlite3.OperationalError:
    # Caso as colunas já existam, ignorar o erro
    pass   

# 2. Atualizando os valores calculados de Bruto e Líquido
cursor_banco_dados.execute('''
UPDATE fato_vendas  
SET 
valor_total_bruto = valor_unitario * quantidade,
    valor_total_liquido = (valor_unitario * quantidade) - valor_desconto;
''')

# 3. Atualizando a classificação de status_venda
cursor_banco_dados.execute('''
UPDATE fato_vendas 
SET status_venda = CASE 
    WHEN valor_total_liquido >= 1500.00 THEN 'Ticket Alto'
    WHEN valor_total_liquido >= 500.00 THEN 'Ticket Médio'
    ELSE 'Ticket Baixo'
END;
''')

conexao_banco_dados.commit()
conexao_banco_dados.close()

print('Etapa 3 concluída: Tabela fato evoluída com sucesso:Regras de negócio de ticket e valores calculados aplicados!')