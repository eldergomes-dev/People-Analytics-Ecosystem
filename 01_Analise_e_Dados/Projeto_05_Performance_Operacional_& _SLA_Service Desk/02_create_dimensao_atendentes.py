"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 02_create_dimensao_atendentes.py
===============================================================================
"""

import sqlite3

# -- 1. Garante que o banco correto está em uso --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- 2. Criar a Tabela Dimensão: dimensao_atendentes --
cursor.execute("""
CREATE TABLE IF NOT EXISTS dimensao_atendentes (
    id_atendente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_atendente TEXT NOT NULL,
    nivel_atendimento TEXT NOT NULL,
    equipe TEXT NOT NULL
);
""")

print("Tabela 'dimensao_atendentes' criada com sucesso!")

# -- SELECT * FROM dimensao_atendentes; --
cursor.execute("SELECT * FROM dimensao_atendentes;")
resultados = cursor.fetchall()

print("Conteúdo atual da tabela 'dimensao_atendentes':", resultados)

# Salva as alterações e fecha a conexão
conexao.commit()
conexao.close()