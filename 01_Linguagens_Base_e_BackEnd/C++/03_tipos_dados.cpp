#include <iostream>
#include <string>
#include <locale>     // Biblioteca de localizacao para o ecossistema C++

int main() {
    // Força a saída do console a respeitar as regras gramaticais da língua portuguesa
    std::setlocale(LC_ALL, "Portuguese");


    // Exemplo de variaveis de diferentes tipos
   std::string nome_do_equipamento = "Braço Robótico Industrial"; // Variável do tipo string
   int unidades_em_estoque = 15;    // Variável do tipo int
   float tensao_alimentacao_float = 220.45f; // Variável do tipo float
   double precisao_calibragem_double = 0.0000045791; // Variável do tipo double
   bool status_manutencao_preventiva = false; // Variável do tipo bool



    // Exibindo os valores das variaveis
    std::cout << "Equipamento identificado: " << nome_do_equipamento << std::endl;
    std::cout << "Unidades em estoque: " << unidades_em_estoque << std::endl;
    std::cout << "Tensão de alimentação Medida (Float): " << tensao_alimentacao_float << "V" << std::endl;
    std::cout << "Métrica de calibragem Fina (Double): " << precisao_calibragem_double<< std::endl;
    std::cout << "Necessidade de Manutenção Preventiva: " << (status_manutencao_preventiva ? "Sim" : "Não") << std::endl;

    return 0;
}