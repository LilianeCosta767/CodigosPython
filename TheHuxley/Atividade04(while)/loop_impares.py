inicio = int(input())
fim = int(input())

valorImpar = inicio

while(valorImpar <= fim):
    if(valorImpar % 2 != 0):
        print(valorImpar)
    valorImpar = valorImpar + 1
