while(1 == 1):
    valores = input().split()
    # print(valores)

    if(valores == []):
        exit(0)

    aux = valores
    cont = 1
    contVetor = []

    i = int(valores[0])
    j = int(valores[1])

    # print('i = ', i)
    # print('j = ', j)

    if(i > 0 and i < 1000000):
        if(j > 0 and j < 1000000):
            for ind in range(i,(j+1)):
                cont = 1
                while(int(aux[ind]) > 1):
                    if(int(aux[ind]) % 2 == 0):
                        i = i / 2
                        cont = cont + 1
                    else:
                        i = (i * 3) + 1
                        cont = cont + 1
                contVetor.append(cont)

        print(valores[0], valores[1], max(contVetor))