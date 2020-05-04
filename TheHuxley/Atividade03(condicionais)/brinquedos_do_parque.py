#programa para verificar se a altura da pessoa permite que ela use o brinquedo do parque

dados = input().split()
F = int(dados[0]) #altura em cm
I = int(dados[1]) #idade

cont = 0 #contador para controlar a quantidade de brinquedos

if(F >= 150 and I >= 12):
    cont = cont + 1
if(F >= 140 and I >= 14):
    cont = cont + 1
if(F >= 170 or I >= 16):
    cont = cont + 1

print('{}\n'.format(cont))