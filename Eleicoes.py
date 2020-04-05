num_voto = 0
alibaba = 0
alcapone = 0
branco = 0
null = 0
votos_validos = 0
percent_alibaba = 0
percent_alcapone = 0

while(num_voto != -1):
    num_voto = int(input())
    if(num_voto != -1):
        if(num_voto == 83):
            alibaba = alibaba + 1 #calculo de x
        elif(num_voto == 93):
            alcapone = alcapone + 1 #calculo de y
        elif(num_voto == 0):
            branco = branco + 1 #calculo de z
        else:
            null = null + 1 #calculo de w
    else: #num_voto == 0
        continue

#impressão de x
print(alibaba)

#impressão de y
print(alcapone)

#impressão de z
print(branco)

#impressão de w
print(null)

#impressao do candidato vencedor = k
if(alibaba > alcapone):
    print('83')
else:
    print('93')

#calculo dos votos validos para percentual
votos_validos = alibaba + alcapone + branco

#calculo do percentual de alibaba = a
percent_alibaba = (alibaba * 100) / votos_validos
print('{:.2f}'.format(percent_alibaba))

#calculo do percentual de alcapone = b
percent_alcapone = (alcapone * 100) / votos_validos
print('{:.2f}'.format(percent_alcapone))