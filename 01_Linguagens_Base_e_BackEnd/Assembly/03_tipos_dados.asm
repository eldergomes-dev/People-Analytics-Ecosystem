; Snippet de código

default rel                ; Diz ao NASM para usar endereçamento relativo (RIP-relative)

section .data
    ; ; db = Define Byte (texto) , dd = Define Double Word (inteiro), dq = Define Quad Word (double)
    ; ; 10 = caractere '\n' (pula linha) , 0 = caractere nulo '\0' (fim de string)
    layout_dados_painel     db "Projeto: %s | Codigo: %d | Custo: R$ %.2f | Precisao: %.6f" ,10, 0
    nome_do_projeto         db "Automacao Comercial" , 0
    codigo_identificador    dd 4589
    custo_operacional       dq 1250.25      ; ; Double de 64 bits carregado em registrador XMM
    precisao_calculo        dq 0.00034182   ; ; Alta precisao armazenada em ponto flutuante

section .text
    global main
    extern printf       ; ; Importamos a funcao nativa do C para renderizar os dados

main:
    ; Aumentamos a pilha para 48 bytes para dar espaço ao 5º argumento
    ; ; Reserva o espaco obrigatorio da pilha no Windows (32 bytes Shadow Space + 8 bytes para o 5º argumento + 8 bytes de alinhamento)
    sub rsp, 48

    ; ; 1º Argumento: Formato da string vai em RCX
    lea rcx, [layout_dados_painel]     

    ; ; 2º Argumento: String do nome vai em RDX
    lea rdx, [nome_do_projeto]

    ; ; 3º Argumento: Inteiro vai em R8d
    mov r8d, [codigo_identificador]

    ; ; 4º Argumento (Ponto Flutuante): DEVE ir para o registrador XMM3 obrigatoriamente!
    movsd xmm3, [custo_operacional]     ; Vai para XMM3 (Regra de ponto flutuante)
    mov r9, [custo_operacional]        ; ADICIONE ESTA LINHA: Copia os mesmos bits para R9 (Regra do Windows x64)


    ; ; 5º Argumento (Ponto Flutuante): Passado via Pilha (Stack) na posição acima do Shadow Space
    movsd xmm0, [precisao_calculo]
    movsd [rsp + 32], xmm0      ; Escreve o 5º argumento logo após os 32 bytes do Shadow Space

    ; ; Dispara a execução do printf
    call printf

    ; ; Sinalizamos o encerramento do processo com sucesso (return 0)
    xor eax, eax

    ; ; Limpa e devolve os 48 bytes da pilha
    add rsp, 48
    ret