N = 0
vetor_aux = []
cont_vetor = 0
matriz = []
aux = 0

#recebe tamanho da matriz
N = int(input())
vetor_aux = [0] * (N*N)
aux = N*N
#cont_vetor = len(vetor_aux)

#preenche a matriz com as posicoes
for i in range(N):
    #vetor_aux = [0] * N
    matriz.append(vetor_aux[:])

#pega todos os valores da matriz e armazena no vetor_aux
for i in range(0, (N*N)):
    aux = int(input())
    vetor_aux[i] = aux


#preenche a matriz
while(aux != 0):
    

#print(matriz)
for l in range(0,N):
    for c in range(0,N):
        print(matriz[l][c], end = ' ')
    print()


#print('vetor_aux = ',vetor_aux)