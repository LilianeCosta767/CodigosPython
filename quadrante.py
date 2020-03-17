#programa que recebe uma coordenada X Y e retorna qual quadrante esse ponto está

numeros = input().split()

X = int(numeros[0])
Y = int(numeros[1])

if(Y == 0 and X != 0):
    print('eixo x')
elif(X == 0 and Y != 0):
    print('eixo y')
elif(X > 0 and Y > 0):
    print('primeiro')
elif(X < 0 and Y > 0):
    print('segundo')
elif(X < 0 and Y < 0):
    print('terceiro')
elif(X > 0 and Y < 0):
    print('quarto')
elif(X == 0 and Y == 0):
    print('origem')