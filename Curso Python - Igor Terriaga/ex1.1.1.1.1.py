def validar(valorLido, minimo, maximo):
    if(valorLido >= minimo and valorLido <= maximo):
        return True
    else:
        return False

valor = int(input('Informe um valor: '))
minimo = 5
maximo = 10

print(validar(valor, minimo, maximo))
