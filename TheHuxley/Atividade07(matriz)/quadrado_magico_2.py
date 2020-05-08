# declarações
N = 0
aux = 0
soma = 0
soma_base = 0
vetor_aux = []

# resolução do problema
N = int(input())
if(N >=2 and N <= 10):
    matriz = []
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
            print('-1')
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
                print('-1')
                exit(0)
        soma = -1

        if(soma == -1):
            soma = 0

            # contando a soma da diagonal 1
            for i in range(N):
                soma = soma + int(matriz[i][i])
            if(soma == soma_base): #se a soma da diagonal 1 for igual à soma_base calculamos a diagonal 2
                soma = 0    
                # contando a soma da diagonal 2-
                c = N - 1
                for l in range(N):
                    soma = soma + int(matriz[l][c])
                    c = c - 1
                if(soma == soma_base):
                    print(soma)
                    exit(0)
                else:
                    print('-1')
                    exit(0)
            else:
                print('-1')

            
