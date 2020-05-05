matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
k = -1

while(k != 0):
    k = int(input())
    if(k == 0):
        break

    # pega os valores da matriz
    for l in range(0,4):
        for c in range(0,4):
            matriz[c][l] = int(input())

    # multiplicando
    for i in range(4):
        matriz[i][i] = matriz[i][i] * k

    for l in range(4):
        for c in range(4):
            print(matriz[l][c], end = ' ')
        print()