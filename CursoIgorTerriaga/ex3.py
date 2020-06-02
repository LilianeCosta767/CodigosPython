quantCigarrosDia = int(input('Quantidade de cigarros fumados por dia: '))
anosFumados = int(input('Fuma a quantos anos?: '))

diasPerdidos = ((10 * quantCigarrosDia) * (anosFumados * 365)) / 1440

print('Você perdeu ', diasPerdidos, ' de vida!')