cod = int(input())
qtd = int(input())

#calculando o valor total da compra
if(cod == 1):
    resul = qtd * 5.30
elif(cod == 2):
    resul = qtd * 6.00
elif(cod == 3):
    resul = qtd * 3.20
elif(cod == 4):
    resul = qtd * 2.50
else:
    print("codigo invalido")

#verificando se o cliente ir� receber o desconto
if(qtd >= 15 or resul >= 40):
    resul = resul - (resul * 0.15)

#imprimindo a sa�da
print('R$ {:.2f}'.format(resul))