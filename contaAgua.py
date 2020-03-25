consumo = int(input())

valor = 7 #valor da taxa

if(consumo <= 10):
    print(valor)
    #break
elif(consumo > 10):
    
    if(consumo >= 20): #20 por causa do intervalo 10-30
        consumo = consumo - 30 #menos 20 desse intervalo e menos 10 da taxa q ja foi inicializada
        valor = valor + (20 * 1)
        print('teste, valor = {}'.format(valor))
        if(consumo == 0):
            print(valor)
    else:
        valor = valor + ((consumo - 10) * 1)
        print(valor)
        #break
if(consumo > 30):
    
    if(consumo >= 70): #70 por causa do intervalo 30-100
        consumo = consumo - 70
        valor = valor + (2 * 70)
        if(consumo == 0):
            print(valor)
    else:
        valor = valor + ((consumo - 10) * 2)
        print(valor)
        #break
if(consumo > 0 and valor > 167):
    valor = valor + (consumo * 5)
    print(valor)

if(consumo > 0 and valor > 7):
    valor = valor + (consumo * 2)
    print(valor)
