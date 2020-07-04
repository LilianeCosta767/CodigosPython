n = 0
cont_casas = 0
dif = 0
valor = 0

while(n != 999):
    n = int(input())
    if(n > 2 and n != 999):
        cont_casas = cont_casas + 1
        dif = n - 2
        valor = valor + (dif * 12.89)

print('{:.2f}'.format(valor))
print(cont_casas)