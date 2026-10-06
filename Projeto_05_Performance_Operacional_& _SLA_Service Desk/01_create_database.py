"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 01_create_database.py
===============================================================================
"""

import sqlite3

# 1. Criar o Banco de Dados e Selecionar (USE db_service_desk)
# O Python conecta ao arquivo do banco relacional. Se ele não existir, é criado na hora

conexao = sqlite3.connect('db_service_desk.db')

print("Banco de dados 'db_service_desk.db' criado e conectado com sucesso!")

# Fecha a conexão após a execução
conexao.close()