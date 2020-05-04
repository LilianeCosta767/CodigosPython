
lista1 = [1,2,4]
lista2 = [3,10,9,7,6]

cont_lista1 = 0
cont_lista2 = 0

intercalada = [0] * (len(lista1) + len(lista2))

print(len(intercalada))

for i in range(len(intercalada)):
    intercalada[i] = lista1[cont_lista1]
    cont_lista1 = cont_lista1 + 1

print (intercalada)