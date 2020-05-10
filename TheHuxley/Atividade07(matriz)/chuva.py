# declarações
N = 0 
matriz = []
aux = 0
vet_aux = []
soma = 0
soma_aux = []
soma_matriz = []

N = int(input())
if(N >= 1 and N <= 100):
    vet_aux = [0] * N
    soma_aux = [0] * N
    for l in range(2*N): # qtd de linhas 
        aux = input().split()
        for c in range(N): # sao N colunas pre-determinadas
            vet_aux[c] = int(aux[c])
        matriz.append(vet_aux[:])

# somando as matrizes
for l in range(N): 
    for c in range(N):
        soma = matriz[l][c] + matriz[l+N][c]
        soma_aux[c] = soma
    soma_matriz.append(soma_aux)
    soma_aux = [0] * N 



for l in range(N):
    for c in range(N):
        print(soma_matriz[l][c], end = ' ')
    print()