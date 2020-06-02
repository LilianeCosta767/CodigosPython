""" Faça um algoritmo que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo. """

retaAB = float(input('Valor da reta AB: '))
retaBC = float(input('Valor da reta BC: '))
retaCA = float(input('Valor da reta CA: '))

if retaAB + retaBC > retaCA and retaAB + retaCA > retaBC and retaBC + retaCA > retaAB:
    print('FORMA UM TRIANGULO')
else:
    print('NAO FORMA UM TRIANGULO')