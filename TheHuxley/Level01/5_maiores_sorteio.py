valores = input().split()

repeticoes = int(valores[0])
digito = int(valores[1])
resul = []
dif = 0

if(digito >= 0 and digito <= 9):
    for i in range(repeticoes):
        num = input()
        if(int(num) >= 0 and int(num) < 10):
            if(int(num) == digito):
                resul.append(int(num))
        elif(int(num) >= 10 and int(num) < 100):
            if(int(num[1]) == digito):
                resul.append(int(num))
        elif(int(num) >= 100 and int(num) < 1000):
            if(int(num[2]) == digito):
                resul.append(int(num))
        elif(int(num) >= 1000):
            print('SEM RESPOSTA')
            exit(0)

    resul = sorted(resul)

    if(len(resul) == 5):
        for i in range(5):
            print(resul[i])

    elif(len(resul) > 5):
        dif = len(resul) - 5
        for i in range(dif, len(resul)):
            print(resul[i])

    elif(len(resul) < 5):
        dif = 5 - len(resul)
        for i in range(dif):
            resul.append(-1)
        resul = sorted(resul)
        for i in range(5):
            print(resul[i])
