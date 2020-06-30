seq = []
cont_vetor = 0
# cont_N = 0
max = 5
num = 0

def imprime_resultado():
    # pega o valor de N
    N = int(input())

    # imprime a saída esperada
    cont_N = 0 # inicializando
    for i in range(len(seq)): 
        if(N == seq[i]):
            cont_N = cont_N + 1
    print(N , " appeared " , cont_N , " times")
    cont_N = 0 # zerando

while (num != -1) :
    # pega os valores
    if (cont_vetor < max) :
        num = int(input()) # pega o numero do usuario
        if (num == -1 and cont_vetor == 0) : # usuario digitou -1 como primeiro numero
            exit(0)
        elif (num == -1 and cont_vetor > 0) :
            imprime_resultado() 

            # sai do programa
            exit(0)

        seq.append(num)    # coloca o valor no vetor
        cont_vetor = cont_vetor + 1

    elif (cont_vetor == max) : # reeniciaremos a contagem de 1000 valores
        imprime_resultado() 
        
        # limpa os dados
        cont_vetor = 0 # limpa o cont_vetor
        seq.clear()    # limpa o vetor
        # cont_N = 0     # limpa o cont_N
        N = 0          # limpa o N


