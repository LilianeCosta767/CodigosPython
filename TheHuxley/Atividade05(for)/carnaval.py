notas = input().split()
maior = 0
menor = 11
soma = 0

for x in notas:
    if(float(x) > maior):
        maior = float(x)
    if(float(x) < menor):
        menor = float(x)

#fazendo a soma das notas:
for y in notas:
    soma = soma + float(y)
soma = soma - (maior + menor)

print('{:.1f}'.format(soma))