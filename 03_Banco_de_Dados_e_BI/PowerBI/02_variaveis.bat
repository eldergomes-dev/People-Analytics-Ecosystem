@echo off

:: ====================================================================
:: CONFIGURAÇÃO INICIAL DO TERMINAL
:: ====================================================================
cls

:: ====================================================================
:: CABEÇALHO VISUAL (O que vai aparecer escrito na tela do CMD)
:: ====================================================================
echo =========================================
echo PROCESSO: ARMAZENAMENTO E EXECUÇÃO DE VARIÁVEIS (M) 
echo =========================================

:: ====================================================================
:: PASSO 1: SIMULAÇÃO DA LÓGICA (Nível 2 - Variável)
:: ====================================================================
::Criamos e armazenamos dados em variáveis locais do Windows via comando SET
set "NOME_DO_DESENVOLVEDOR=Elder"
set "STATUS_DO_PROJETO=Homologado e Ativo"

:: Exibibimos em tela os valores armazenadossimulanddo as saídas do power Qwery
echo [DADO PROCURADO] Desenvolvedor responsavel: %NOME_DO_DESENVOLVEDOR%
echo [STATUS ATUAL] Situacao Cadastral:          %STATUS_DO_PROJETO%
echo ==========================================================================
echo.

::=============================================================================
:: PASSO 2: EXECUTAR A AUTOMAÇÃO (Ação no Windows abre o PowerBI)
::=============================================================================
echo [AUTOMAÇÃO] Disparando inicializacao do dashboard no Power BI Desktop...

:: O terminal invoca o arquivo binário nativo .pibx da nossa aula de variaáveis
start "" "02_variaveis.pbix"

::=============================================================================
:: FINALIZAÇÃO DO SCRIPT
::=============================================================================
echo Execução concluída com suvesso absoluto!
pause