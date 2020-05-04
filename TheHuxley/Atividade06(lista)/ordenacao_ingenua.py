n = int(input())

vetor = [0] * n

#pega os valores
for i in range(n):
    vetor[i] = int(input())

#ordena
vetor.sort()

for i in range(n):
    print('[', end = '')
    print(vetor[i], end  = '')
    print(']', end = '')