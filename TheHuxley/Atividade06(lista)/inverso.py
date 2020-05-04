N = int(input())
valores = input().split()

numeros = [0] * N

#atribuicao no vetor
for i in range(N):
    numeros[i] = int(valores[i])

#inverte o vetor
resul = numeros[::-1]

for i in range(N):
    print(resul[i], end = ' ')