// 1. DECLARAÇÃO DE VARIÁVEIS: Alocamos dados em constantes com padrão Camel Case
const nomeDoUsuarioLogado = "João";
const tipoPerfilDeAcesso = "Consultor Sênior";

// 2. EXIBIÇÃO EM TELA: Capturamos os elementos HTML pelos seus IDs e alteramos o texto de forma limpa
document.getElementById("nome_do_usuario_display").textContent ="Bem Vindo: " + nomeDoUsuarioLogado;
document.getElementById("perfil_acesso_display").textContent = "Nível de permissão: " + tipoPerfilDeAcesso;

// 3.(ALERTA): Somamos um alerta na tela do navegador resgatando os dados das variáveis anteriores
alert("Sessão iniciada com Sucesso! Usuário: " + nomeDoUsuarioLogado + " [ " + tipoPerfilDeAcesso + "]");