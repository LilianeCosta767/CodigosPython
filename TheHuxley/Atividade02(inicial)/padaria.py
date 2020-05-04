total_broa = float(input())
total_pao = float(input())

valor_poupanca = (total_broa * 1.50) + (total_pao * 0.20)
valor_poupanca = valor_poupanca * 0.1

print('O valor a ser guardado na poupan�a ser� R$ {:.2f}'.format(valor_poupanca))