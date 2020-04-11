#ampulhetas
largura_amp = 0
qtd_pontos = 0
ind_matriz = 0
cont_atribuicao = 0 #contador para atribuição do vetor da ampulheta

N_casos = int(input()) #valores de casos
if(N_casos >= 0):
    contAmpulheta = 0

    while contAmpulheta <= N_casos: #pega os valores de l e i
        altura_amp = int(input())
        altura_pontos = int(input())
        if altura_amp > 3 and altura_amp < 40:
            if altura_pontos < (altura_amp - 2):
                #criação da matriz
                matriz_ampulheta = [[] * altura_amp, [] * largura_amp]

                #contagem da largura da ampulheta
                largura_amp = N_casos+altura_amp+altura_pontos
                if(largura_amp % 2 == 0): #verifica se é par
                    largura_amp = largura_amp + 1 #largura final da ampulheta
                else:
                    largura_amp = largura_amp + 2

                #contagem dos pontos de areia
                qtd_pontos = largura_amp - 6

                #atualizando altura da ampulhera
                altura_amp = altura_amp * 2
                ind_matriz = altura_amp

                #atribuição da ampulheta
                for ind_matriz in range(len(altura_amp)): #percorre as linhas
                    while(cont_atribuicao <= largura_amp): #percorre as colunas
                        if(cont_atribuicao == 0 or cont_atribuicao == 1):
                            matriz_ampulheta[ind_matriz][cont_atribuicao] = '*'
                        elif(cont_atribuicao == largura_amp or cont_atribuicao == (largura_amp - 1)):
                            matriz_ampulheta[ind_matriz][cont_atribuicao] = '*'
                        elif(matriz_ampulheta[ind_matriz-1] == '*'):
                            matriz_ampulheta[ind_matriz][cont_atribuicao] = ' *'

                        # elif(ind_vet == (altura_amp / 2) or ind_vet == (altura_amp / 2) + 1): #encontra o meio da ampulheta
                        #     vet_ampulheta[ind_vet] = '?'
                        cont_atribuicao = cont_atribuicao + 1
                    ind_vet = ind_vet - 1

                #ind_vet = 0 #zerando o indice

                #impressão da ampulheta
                for ind_vet in range(len(altura_amp)):
                    print(matriz_ampulheta)

                contAmpulheta = contAmpulheta + 1 #vai para proxima ampulheta
