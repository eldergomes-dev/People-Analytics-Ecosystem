<?php

// Armazenamento de tipos de dados dinâmicos utilizando o prefixo obrigatório '$'
$nome_do_fornecedor = "Inúdustrias Metalúrgicas S.A."; // String
$total_pedidos_compra = 87;                            // Integer
$valor_frete_float = 450.75;                           // Float/Double padrao do PHP
$coeficiente_atrito_double = 0.0034198523;             // Double de alta precisao
$status_fornecimento_bloqueado = false;                // Boolean

// Exibição dos dados encadeados no terminal

echo "Razão Social do Fornecedor: " . $nome_do_fornecedor . "\n";
echo "Total de Pedidos de Compra Ativos: " . $total_pedidos_compra . "\n";
echo "Custo do Frete (Float): R$ " . $valor_frete_float . "\n";
echo "Coeficiente de Atrito (Double): " . $coeficiente_atrito_double . "\n";
echo "Alerta de Restrição Comercial: " . ($status_fornecimento_bloqueado ? "Fornecedor Bloqueado" : "Fornecedor Ativo") . "\n";



?>