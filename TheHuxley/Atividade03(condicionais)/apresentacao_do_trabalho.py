valores = input().split()

IG = int(valores[0]) #interface grafica
IA = int(valores[1]) #inteligencia artificial
E = int(valores[2]) #encapsulamento
I = int(valores[3]) #indentação
S = int(valores[4]) #struct

if((IG == 1 or IA == 1) and (E == 1 and I == 1) and S ==1):
    print('AVALIADO\n')
else:
    print('0\n')