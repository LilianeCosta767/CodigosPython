motores = []
aux = 0
vetor_aux = [0] * 2
custo = []
motor_resultado = []

#pega os dados da maquina
for mes in range(12):
    aux = input().split()
    for i in range(2):
        vetor_aux[i] = int(aux[i])
    motores.append(vetor_aux[:])

#pega os valores do custo e lucro
for i in range(2):
    aux = input().split()
    for j in range(2):
        vetor_aux[i] = float(aux[i])
    custo.append(vetor_aux[:])

print('custo = ', custo)

#multiplicacao
for a in range(12): #laço para motor_resultado
    for l in range(12): #laço para motores e custo
        aux = 0
        for c in range(2):
            motor_resultado[a] += motores[l][c] * custo[c][aux]
            aux = aux + 1

#saida
for a in range(12): #laço para motor_resultado
    for l in range(12): #laço para motores e custo
        for c in range(2):
            print('Motor[{}], Mes[{}], custo=[{}], lucro=[{}]'.format(a, l, custo[0][c], custo[1][c]))
    print()


#print('motores = ', motores)