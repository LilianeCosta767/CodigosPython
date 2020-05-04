valores_1 = input().split()
valores_2 = input().split()

array_1 = []
array_2 = []
array_diferenca = []

for i in range(len(valores_1)):
    array_1.append(int(valores_1[i]))


for i in range(len(valores_2)):
    array_2.append(int(valores_2[i]))

for i in range(len(array_1)):
    if(array_1[i] in array_2):
        pass
    else:
        array_diferenca.append(array_1[i])

array_diferenca.sort()
array_diferenca.reverse()

for i in range(len(array_diferenca)):
    print(array_diferenca[i], end = ' ')

