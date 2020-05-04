valores = input().split()
agua = float(valores[0])
esgoto = float(valores[1])

valor_agua = agua * esgoto * 1000
valor_esgoto = 0.8 * valor_agua
valor_total = valor_agua + valor_esgoto

print('{:.2f}'.format(valor_agua))
print('{:.2f}'.format(valor_esgoto))
print('{:.2f}'.format(valor_total))