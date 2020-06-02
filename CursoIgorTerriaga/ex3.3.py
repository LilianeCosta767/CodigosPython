#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Qual a distância em Kms?: '))
velocidade = float(input('Qual a velocidade em Kms/h?: '))

print(distancia/velocidade * 60, 'minutos')