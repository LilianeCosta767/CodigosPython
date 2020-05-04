numeros = input().split()

x = int(numeros[0])
y = int(numeros[1])

while x <= y:
    if(x > 0 and x < 100): # verifica de é positivo e menor que 100
        esq = int(x/10) #pega o digito da esquerda
        dir = int(x%10) #pega o digito da direita
        if(dir != 0): #verifica se nao termina em 0
            if(x%esq == 0): #verifica se o resto é divisivel pelo original
                print(x)
    x = x + 1