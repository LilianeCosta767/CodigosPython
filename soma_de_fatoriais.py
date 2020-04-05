numeros = [0,0,0,0,0]
fatorial = [0,0,0,0,0]
resultado = 0
count = 0

#pegando os valores do usuario
for i in range(0,5):
    num = int(input())
    numeros[i] = num

#calculando o fatorial de cada valor
for i in range(0,5):
    count = numeros[i]
    k = numeros[i]
    if(numeros[i] == 0):
        fatorial[i] = 1
        continue
    if(numeros[i] == 1):
        fatorial[i] = 1
        continue
    while(count > 1):
        k = k * (count - 1) #atualizando o valor do fatorial
        count = count - 1 #atualizando o controlador do while
    fatorial[i] = k

#separando os fatoriais multiplos de 3
for i in range(0,5):
    if(numeros[i] % 3 == 0):
        resultado = resultado + fatorial[i]

print(resultado)