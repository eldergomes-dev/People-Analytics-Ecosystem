// Armazenamos dados de rastreamento de clique ou conversão dentro de variáveis semânticas
nomeDoUsuarioAnalise = "Elder";
categoriaDoPlanoSelecionado = "Premium_Automation";

// Estruturamos o objeto de auditoria alimentando o Analytics com as variáveis criadas
const eventMapeamentoVariaveis = {
    'event': 'registro_variaveis_usuario' ,
    'usuario_identificado' : nomeDoUsuarioAnalise,
    'plano_usuario' : categoriaDoPlanoSelecionado

};

// Disparamos o objeto populado para a camada de gerenciamento de tags global
window.dataLayer = window.dataLayer || [];
window.dataLayer.push(eventMapeamentoVariaveis);