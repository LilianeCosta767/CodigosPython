# contadores
cont_laco = 0
cont_times = 0 

# vetores para cada campeonato
oitavas_final = [0] * 8
quartas_final = [0] * 4
semifinais    = [0] * 2
final         = [0] * 1


resultado_jogos = [0] * 2


times_oitavas_final = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
times_quartas_final = []
times_semifinais    = []
times_final         = []


while(cont_laco < 8): # laço das oitavas de final
    valores = input().split()
    resultado_jogos[0] = int(valores[0])
    resultado_jogos[1] = int(valores[1])
    oitavas_final[cont_laco] = resultado_jogos # primeiro jogo
    if(resultado_jogos[0] >= 0 and resultado_jogos[0] <= 20):
        if(resultado_jogos[1] >= 0 and resultado_jogos[1] <= 20):
            if(oitavas_final[cont_laco][0] > oitavas_final[cont_laco][1]):
                times_quartas_final.append(times_oitavas_final[cont_times])
            elif(oitavas_final[cont_laco][0] < oitavas_final[cont_laco][1]):
                times_quartas_final.append(times_oitavas_final[cont_times + 1])
    cont_times = cont_times + 2
    cont_laco = cont_laco + 1

cont_laco  = 0
cont_times = 0

while(cont_laco < 4): # laço das quartas de final
    valores = input().split()
    resultado_jogos[0] = int(valores[0])
    resultado_jogos[1] = int(valores[1])
    quartas_final[cont_laco] = resultado_jogos # primeiro jogo
    if(resultado_jogos[0] >= 0 and resultado_jogos[0] <= 20):
        if(resultado_jogos[1] >= 0 and resultado_jogos[1] <= 20):
            if(quartas_final[cont_laco][0] > quartas_final[cont_laco][1]):
                times_semifinais.append(times_quartas_final[cont_times])
            elif(quartas_final[cont_laco][0] < quartas_final[cont_laco][1]):
                times_semifinais.append(times_quartas_final[cont_times + 1])
    cont_times = cont_times + 2
    cont_laco = cont_laco + 1

cont_laco  = 0
cont_times = 0

while(cont_laco < 2): # laço da seminal
    valores = input().split()
    resultado_jogos[0] = int(valores[0])
    resultado_jogos[1] = int(valores[1])
    semifinais[cont_laco] = resultado_jogos # primeiro jogo
    if(resultado_jogos[0] >= 0 and resultado_jogos[0] <= 20):
        if(resultado_jogos[1] >= 0 and resultado_jogos[1] <= 20):
            if(semifinais[cont_laco][0] > semifinais[cont_laco][1]):
                times_final.append(times_semifinais[cont_times])
            elif(semifinais[cont_laco][0] < semifinais[cont_laco][1]):
                times_final.append(times_semifinais[cont_times + 1])
    cont_times = cont_times + 2
    cont_laco = cont_laco + 1

cont_laco  = 0
cont_times = 0

while(cont_laco < 2): # laço da final
    valores = input().split()
    resultado_jogos[0] = int(valores[0])
    resultado_jogos[1] = int(valores[1])
    final[cont_laco] = resultado_jogos # primeiro jogo
    if(resultado_jogos[0] >= 0 and resultado_jogos[0] <= 20):
        if(resultado_jogos[1] >= 0 and resultado_jogos[1] <= 20):
            if(final[cont_laco][0] > final[cont_laco][1]):
                print(times_final[0])
                break
            elif(final[cont_laco][0] < final[cont_laco][1]):
                print(times_final[1])
                break