-- Criamos as variaveis de sessao respeitando os tipos e mapeando em precisao na memoria
SET @nome_do_servidor_ti := "Servidor AWS Central";
SET @limite_usuarios_conexao := 2500;
SET @taxa_perda_pacote_float := 0.025;           -- representando valor em Float
SET @precisao_calculo_double := 4587.9321458742; -- Armazenando um valor Double pesado

-- Executamos a projecao limpa sem o CAST para rodar direto na memoria da sessao
SELECT
    @nome_do_servidor_ti AS host_servidor,
    @limite_usuarios_conexao AS capacidade_usuarios,
    @taxa_perda_pacote_float AS perda_rede_float,
    @precisao_calculo_double AS metrica_precisao_double;
    