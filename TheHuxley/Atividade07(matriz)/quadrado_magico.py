# declarações
N = 0
aux = 0
soma = 0
soma_base = 0
vetor_aux = []

# resolução do problema
print('Digite a dimensao da matriz quadrada N x N:')
N = int(input())
if(N >=2 and N <= 10):
    matriz = []
    print('Digite os elementos da matriz:')
    for l in range(N):
        aux = input().split()
        matriz.append(aux)

    # verificando valor de alguma soma
    for i in range(N):
        soma_base = soma_base + int(matriz[0][i])

    # contando a soma das linhas
    for j in range(N):
        for i in range(N):
            soma = soma + int(matriz[j][i]) # calculando a soma das linhas
        if(soma == soma_base):
            soma = 0
            continue
        else:
            print('Os elementos NAO FORMAM um quadrado magico.')
            exit(0)
    soma = -1

    if(soma == -1):
        soma = 0

        # contando a soma das colunas
        for j in range(N):
            for i in range(N):
                soma = soma + int(matriz[i][j]) # calculando a soma das colunas
            if(soma == soma_base):
                soma = 0
                continue
            else:
                print('Os elementos NAO FORMAM um quadrado magico.')
                exit(0)
        soma = -1

        if(soma == -1):
            soma = 0

            # contando a soma da diagonal
            for i in range(N):
                soma = soma + int(matriz[i][i])
            if(soma == soma_base):
                print('Os elementos FORMAM um quadrado magico.')
                print('A soma do quadrado magico e {}.'.format(soma_base))
            else:
                print('Os elementos NAO FORMAM um quadrado magico.')
