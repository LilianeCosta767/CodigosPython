from datetime import date

nome = input('Nome: ')
dataAtual = date.today()
print(dataAtual)
quantDiasAluguel = int(input('Quantidade de dias de aluguel: '))

print("""
Nome: {}
Data de entrega do veículo: {}-{}-{}
""".format(nome, dataAtual.day + quantDiasAluguel, dataAtual.month, dataAtual.year))