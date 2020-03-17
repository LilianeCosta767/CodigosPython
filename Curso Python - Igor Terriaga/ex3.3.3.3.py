""" Faça um programa que receba a quantidade de termos e a
razão de uma progressão aritmética, então imprima a soma
de todos os seus termos. """

numTermos = int(input('Numero de termos: '))
razao = int(input('Razao da progressao: '))
soma = 0
for i in range(0, numTermos, razao):
    soma = soma + i

print(soma)