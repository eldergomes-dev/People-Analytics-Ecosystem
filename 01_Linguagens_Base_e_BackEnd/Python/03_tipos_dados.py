# Declaramos os diferentes tipos de dados com semântica corporativa clara
nome_do_produto = "Servidor Dedicado Alpha" # String
quantidade_licencas_ativas = 142            # Integer
faturamento_minimo_estimado = 12500.75      # Float/Double de precisao padrão
margem_lucro_precisa = 0.158739215          # Double simulado por alta precisão
indicador_sistema_operacional = True        # Boolean

# Exibição dos tipos de dados e seus valores
print(f"Nome do produto: {nome_do_produto} (Tipo: {type(nome_do_produto)})")
print(f"Quantidade de licenças ativas: {quantidade_licencas_ativas} (Tipo: {type(quantidade_licencas_ativas)})")
print(f"Faturamento mínimo estimado: {faturamento_minimo_estimado} (Tipo: {type(faturamento_minimo_estimado)})")
print(f"Margem de lucro precisa: {margem_lucro_precisa} (Tipo: {type(margem_lucro_precisa)})")
print(f"Indicador de sistema operacional: {indicador_sistema_operacional} (Tipo: {type(indicador_sistema_operacional)})")