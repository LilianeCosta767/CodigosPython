altura_amp = 5
largura_amp = 2

matriz_ampulheta = [[] * altura_amp, [] * largura_amp]

for ind_linha in range(altura_amp):
    for ind_coluna in range(largura_amp):
        print(matriz_ampulheta[ind_linha][ind_coluna], end = ' ')
    print()