#Escreva um programa que verifique se um ano é bissexto.
ano = int(input('Informe o ano: '))

if ano%4 == 0 and ano%100 != 0:
    print('Bissexto')
else:
    print('Não é bissexto')