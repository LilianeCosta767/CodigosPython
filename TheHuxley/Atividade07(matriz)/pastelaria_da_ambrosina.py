# declarações
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
aux = 0
valor = [0] * 3
soma = 0

# resolução do problema
for l in range(4): #percorre as linhas
    #for i in range(4): #leitura da linha como um input
    aux = input().split()
    for c in range(4): #atribuição da linha informada na linha correspondente da matriz
        matriz[l][c] = float(aux[c])


# fazendo a conta dos preços do pastel
for l in range(3): # pegaremos apenas a linha do produto
    for c in range(4): # pegamos todas as colunas
        soma = soma +  (matriz[3][c] * matriz[l][c])
    valor[l] = soma
    soma = 0

# imprimindo o resultado
for i in range(3):
    print('{:.2f}'.format(valor[i]))