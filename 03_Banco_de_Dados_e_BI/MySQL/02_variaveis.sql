-- Criamos variáveis de sessão em memória utilizando o caractere '@' e o operador ':='
SET @nome_do_cliente_sistema := "João Pedro";
SET @pontuacao_score_credito := 850;

-- Projetamos uma tabela virtual em tela resgatando e exibindo as variáveis armazenadas
SELECT
	@nome_do_cliente_sistema AS cliente_identificado,
    @pontuacao_score_credito AS score_credito_atualizado;