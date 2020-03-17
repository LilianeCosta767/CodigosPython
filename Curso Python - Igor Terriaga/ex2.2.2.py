""" Faça um algoritmo que leia 2 números e informe qual é o
maior dentre eles, ou se são iguais. """

numero1 = int(input('Informe o 1º número: '))
numero2 = int(input('Informe o 2º número: '))

if numero1 > numero2:
    print('O número %d é maior.' %(numero1))
elif numero1 < numero2:
    print('O número %d é maior.' %(numero2))
else:
    print('Os números possuem valores iguais!')