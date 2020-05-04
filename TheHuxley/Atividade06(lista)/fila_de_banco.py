qtd_fila_n = 0 # valor de n, representa a qtd de pessoas da fila n
qtd_fila_m = 0 # valor de m, representa a qtd de pessoas da fila m
vetor_fila_n = []
vetor_fila_m = []
saiu_almoco = 0

qtd_fila_almoco = 0
fila_almoco = []

valores = input().split()

qtd_fila_n = int(valores[0])
if(qtd_fila_n >= 0 and qtd_fila_n <= 10000):
    qtd_fila_m = int(valores[1])
    if(qtd_fila_m >= 0 and qtd_fila_m <= 10000):
        # fila que vai se integrar a outra
        saiu_almoco = int(valores[2])

        # atualizacao da qtd_fila_almoco
        qtd_fila_almoco = qtd_fila_m + qtd_fila_n

        # valores da fila n
        for i in range(qtd_fila_n):
            vetor_fila_n.append(int(input()))

        # valores da fila m
        for i in range(qtd_fila_m):
            vetor_fila_m.append(int(input()))

        #print('vetor m = ', vetor_fila_m)
        # composicao do vetor_almoco
        if(saiu_almoco == 2):
            for i in range(qtd_fila_almoco):
                # if(i > qtd_fila_n and i > qtd_fila_m):
                #     break
                if(i < qtd_fila_n):
                    fila_almoco.append(vetor_fila_n[i])
                if(i < qtd_fila_m):
                    fila_almoco.append(vetor_fila_m[i])
                else:
                    continue
        else:
            for i in range(qtd_fila_almoco):
                if(i < qtd_fila_m):
                    fila_almoco.append(vetor_fila_m[i])
                if(i < qtd_fila_n):
                    fila_almoco.append(vetor_fila_n[i])
                else:
                    continue

for i in range(qtd_fila_almoco):
    print(fila_almoco[i])