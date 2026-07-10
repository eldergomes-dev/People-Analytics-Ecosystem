#include <stdio.h>
#include <stdbool.h>
#include <locale.h>    // Biblioteca obrigatoria para configuracao de idioma local

int main() {

    // Configura o terminal do Windows para aceitar a acentuacao correta em portugues
    setlocale(LC_ALL, "Portuguese");

    // Declaracao rigorosa e estatica de todos os tipos primitivos de mercado
    char nome_do_usuario[] = "Joao da Silva"; // String/Vetor de caracteres para armazenar texto
    int id_transacao_bancaria = 74125; // Tipo de dado primitivo para armazenar numeros inteiros
    float taxa_operacao_float = 14.50f; // Float (Precisao simples - 32 bits, exige sufixo 'f')
    double margem_lucro_double = 1547.859321;   // Double (Precisao dupla - 64 bits)
    bool validador_autenticacao = true; // Tipo de dado booleano (true ou false)

    // Exibicao dos dados usando seus respectivos formatadores nativos (%f para float, %lf para double)

    printf("Nome do usuario: %s\n", nome_do_usuario);
    printf("ID da transacao bancaria: %d\n", id_transacao_bancaria);
    printf("Taxa de operacao (float): %.2f\n", taxa_operacao_float);
    printf("Margem de lucro (double): %.6lf\n", margem_lucro_double);
    printf("Validador de autenticacao: %s\n", validador_autenticacao ? "Ativo" : "Nao Inativo");

    return 0;
}