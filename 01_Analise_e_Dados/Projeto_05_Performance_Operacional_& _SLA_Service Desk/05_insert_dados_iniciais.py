"""
===============================================================================
PROJETO 05: Performance Operacional & SLA de Service Desk
ARQUIVO: 05_insert_dados_iniciais.py
===============================================================================
"""

import sqlite3

# -- 1. Garante que o banco correto está em uso --
conexao = sqlite3.connect("db_service_desk.db")
cursor = conexao.cursor()

# -- Desativa a checagem de chaves estrangeiras --
# cursor.execute("PRAGMA foreign_keys = OFF;")

# -- Limpa as tabelas (equivalente ao TRUNCATE TABLE) e zera os IDs --
# cursor.execute("DELETE FROM fato_chamados;")
# cursor.execute("DELETE FROM dimensao_atendentes;")
# cursor.execute("DELETE FROM dimensao_categorias;")  
# cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('fato_chamados', 'dimensao_atendentes', 'dimensao_categorias') ;")

# -- Reativa a checagem de chaves estrangeiras --
# cursor.execute("PRAGMA foreign_keys = ON;")




# -- 5. Inserir Dados Iniciais para Testes --
cursor.execute("""
    INSERT INTO dimensao_atendentes (nome_atendente, nivel_atendimento, equipe) VALUES
    ('Elder Gomes', 'N3', 'Infraestrutura'),
    ('Mariana Silva', 'N1', 'Suporte Usuario'),
    ('Carlos Eduardo', 'N2', 'Sistemas');
""")
    
# -- Inserindo Categorias de SLA --
cursor.execute("""
    INSERT INTO dimensao_categorias (nome_categoria, sla_horas_limite) VALUES
    ('Acessos e Permissoes', 4),
    ('Hardware e Impressoras', 24),
    ('instabilidade de Sistema', 8);
""")

# -- Inserindo Chamados --
cursor.execute("""
INSERT INTO fato_chamados (id_atendente, id_categoria, data_abertura, data_fechamento, tempo_resolucao_horas, status_chamado, cumpre_sla) VALUES
(1, 3, '2026-05-01 08:00:00', '2026-05-01 12:30:00', 4.50, 'Fechado', 'Sim'),
(2, 1, '2026-05-01 09:15:00', '2026-05-01 15:00:00', 5.75, 'Fechado', 'Nao'),
(3, 2, '2026-05-02 10:00:00', '2026-05-03 09:00:00', 23.00, 'Fechado', 'Sim'),
(1, 3, '2026-05-03 14:00:00', NULL, NULL, 'Em Aberto', 'Nao');
""")

# Confirma as alterações no banco de dados
conexao.commit()
print("Dados inseridos com sucesso!")

# -- SELECTs de verificação --
print("\n--- DIMENSAO ATENDENTES ---")
cursor.execute("SELECT * FROM dimensao_atendentes;")
print(cursor.fetchall())

print("\n--- DIMENSAO CATEGORIAS ---")
cursor.execute("SELECT * FROM dimensao_categorias;")
print(cursor.fetchall())

print("\n--- FATO CHAMADOS ---")
cursor.execute("SELECT * FROM fato_chamados;")
print(cursor.fetchall())

# Fecha a conexão
conexao.close()