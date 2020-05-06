# declarações
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
aux = 0
#cont_aux = 0

# resolução do problema
# pegando os valores da matriz
for l in range(4):
    for c in range(4):
        aux = input().split()
        for i in range(4):
            matriz[l][c] = float(aux[i])
    
# imprimindo a matriz
for l in range(4):
    for c in range(4):
        print(matriz[l][c], end = ' ')
    print()
