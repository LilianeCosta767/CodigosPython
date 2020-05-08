# declarações
N = 0 
matriz = []

N = int(input())
if(N >= 1 and N <= 100):
    for l in range(2*N): # qtd de linhas 
        aux = input().split()
        for c in range(N): # sao N colunas pre-determinadas
            matriz[l][c] = int(aux[c])

for l in range(2*N):
    for c in range(N):
        print(matriz)
    print()
