""" Faça um programa que leia um numero de 0 a 9999 e
mostre na tela cada um dos dígitos separados. """

numero = int(input('Informe um número de 0 a 9999: '))

unidade = numero%10;
dezena = numero%100;
centena = numero%1000;
milhar = numero%10000;

print('Unidade:',unidade//1)
print('Dezena:',dezena//10)
print('Centena:',centena//100)
print('Milhar:',milhar//1000)