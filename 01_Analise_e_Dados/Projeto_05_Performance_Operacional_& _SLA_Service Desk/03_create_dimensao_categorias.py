"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 03_create_dimensao_categorias.py
===============================================================================
"""

import sqlite3

# -- 1. Garante que o banco correto está em uso --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- 2. Criar a Tabela Dimensão: dimensao_categorias --
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dimensao_categorias (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL,
        sla_horas_limite INTEGER NOT NULL
);
""")

print("Tabela 'dimensao_categorias' criada com sucesso!")

# -- SELECT * FROM dimensao_categorias; --
cursor.execute("SELECT * FROM dimensao_categorias;")
resultados = cursor.fetchall()

print("Conteúdo atual da tabela 'dimensao_categorias':",resultados)

# Salva as alterações e fecha a conexão
conexao.commit()
conexao.close()