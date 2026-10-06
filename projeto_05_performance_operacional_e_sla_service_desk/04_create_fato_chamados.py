"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 04_create_fato_chamados.py
===============================================================================
"""

import sqlite3  

# -- 1. Garante que o banco correto está em uso --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- 4. Criar a Tabela Fato: fato_chamados --
cursor.execute("""
    CREATE TABLE IF NOT EXISTS fato_chamados (
        id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
        id_atendente INTEGER,
        id_categoria INTEGER,
        data_abertura TEXT NOT NULL,
        data_fechamento TEXT,
        tempo_resolucao_horas REAL,
        status_chamado TEXT NOT NULL,
        cumpre_sla TEXT NOT NULL,
        FOREIGN KEY (id_atendente) REFERENCES dim_atendentes(id_atendente),
        FOREIGN KEY (id_categoria) REFERENCES dim_categorias(id_categoria)
);
""")

print("Tabela fato_chamados criada com sucesso!")

# -- SELECT * FROM fato_chamados; --
cursor.execute("SELECT * FROM fato_chamados;")
resultados = cursor.fetchall()

print("Conteúdo atual da tabela 'fato_chamados':", resultados)

# Salva as alterações e fecha a conexão
conexao.commit()    
conexao.close()