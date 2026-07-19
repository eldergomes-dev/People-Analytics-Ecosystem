@echo off
::==========================================================
:: CONFIGURAÇÃO INICIAL DO TERMINAL
::==========================================================
cls

::==========================================================
:: CABEÇALHO VISUAL DO PROCESSO
::==========================================================        
echo ==========================================================
echo PROCESSO: TRIAGEM E CLASSIFICACAO DE TIPOS DE DADOS
echo ==========================================================

::==========================================================
:: PASSO 1: SIMULAÇÃO LOCAL DAS VARIÁVEIS (Incluindo Float e Double)
::==========================================================
set "NOME_DO_MODULO =Motor de Automação ETL"
set "CONTADOR INTEIRO=500"
set "PERCENTUAL_FLOAT=98.45"
set "VARIANCIA_DOUBLE=0.000341985215"
set "STATUS_BOOLEAN=TRUE"

echo [TEXTO] Modulo Carregado: %NOME_DO_MODULO%
echo [INTEIRO] Iteracoes Executadas: %CONTADOR INTEIRO%
echo [FLOAT] Percentual Eficiencia: %PERCENTUAL_FLOAT%
echo [DOUBLE] Variancia analitica: %VARIANCIA_DOUBLE%
echo [BOOLEAN] Status do Processo: %STATUS_BOOLEAN%
echo ==========================================================
echo.

::==========================================================
:: PASSO 2:EXECUÇÃO DA AÇÃO CORPORATIVA (Simulação de Processamento)
::==========================================================
echo [AUTOMAÇÃO] Inicializando o dashboard de tipos de dados no PowerBi...
start "" "03_tipos_dados.pbix"

echo Processamento finalizado com sucesso!
pause