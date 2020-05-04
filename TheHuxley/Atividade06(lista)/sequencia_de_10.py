cont = 0
vetor = [0] * 10

valores = input().split()

for i in range(10):
    vetor[i] = int(valores[i])

#comparação
for i in range(10):
    if(vetor[9] == vetor[i]):
        cont = cont + 1

print('O numero', vetor[9], 'apareceu', cont, 'vezes')