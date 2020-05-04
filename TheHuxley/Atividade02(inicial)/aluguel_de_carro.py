qtd_dia = int(input())
qtd_km = float(input())

valor_total = (30 * qtd_dia) + (0.01 * qtd_km)
valor_total = valor_total - (valor_total * 0.1)

print('{:.2f}'.format(valor_total))