// See https://aka.ms/new-console-template for more information

// Declaração de Tipos de dados em C#
        string nomeDoInvestidor = "João Silva"; // Variável do tipo string para armazenar o nome do investidor
        int numeroDeAtivosComprados = 540; // Variável do tipo int para armazenar o número de ativos comprados
        float cotacaoInicialFloat = 23.45f; // Variável do tipo float para armazenar a cotação inicial do ativoFloat (Exige o sufixo 'f')
        double patrimonioLiquidoDouble = 1258900.4578; // Variável do tipo double para armazenar o patrimônio líquido, Double (Precisao monetaria/estatistica)
        bool contaInvestimentosVerificada = true; // Booleano para indicar se a conta de investimentos foi verificada
        
        
        
        // Exibindo os valores das variáveis
        Console.WriteLine("Nome do Investidor: " + nomeDoInvestidor);
        Console.WriteLine("Número de Ativos Comprados: " + numeroDeAtivosComprados);
        Console.WriteLine("Preço de Compra Inicial (Float): R$ " + cotacaoInicialFloat);
        Console.WriteLine("Patrimônio de Auditoria (Double): R$ " + patrimonioLiquidoDouble);
        Console.WriteLine("Conta Homologada no Sistema: " + (contaInvestimentosVerificada ? "Sim" : "Não"));