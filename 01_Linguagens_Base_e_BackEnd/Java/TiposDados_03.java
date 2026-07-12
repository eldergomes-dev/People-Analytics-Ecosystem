public class TiposDados_03 {
    public static void main(String[] args) {
        // Declaração de Tipos de Dados em Java
        String nomeDaEmpresaParceira = "Logística Global S.A."; // Tipo String
        int totalDeContainersDescarregados = 320;               // Tipo integer
        float pesoCargaFloat = 15400.85f;                       // Float (Exige sufixo 'f')
        double taxaImportacaoDouble = 0.045719325;              // Double (Precisao cirurgica)
        boolean manifestoCargaLiberado = true;                  // Boolean (true ou false)
        

        // Saída padrão formatada do sistema Java

        System.out.println("Empresa Fornecedora: " + nomeDaEmpresaParceira);
        System.out.println("Contêineres Processados: " + totalDeContainersDescarregados);
        System.out.println("Peso Liquido Medido (Float): " + pesoCargaFloat + " kg");
        System.out.println("Alíquota Aplicável (Double): " + taxaImportacaoDouble);
        System.out.println("Despacho Aduaneiro Autorizado: " + manifestoCargaLiberado);
    }
}