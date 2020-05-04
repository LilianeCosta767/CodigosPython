#questão ampulheta

largura_amp = 0
qtd_pontos = 0
ind_matriz = 0
cont_atribuicao = 0 #contador para atribuição do vetor da ampulheta
ind_linha = 0
ind_coluna = 0


N_casos = int(input()) #valores de casos
if(N_casos >= 0):
    cont_ampulheta = 0 #contador de ampulhetas

    while cont_ampulheta <= N_casos: 
        print('entrei no while')
        altura_amp = int(input()) #valor de l
        altura_pontos = int(input()) #valor de i
        if altura_amp > 3 and altura_amp < 40:
            if altura_pontos < (altura_amp - 2):
                #contagem da largura da ampulheta
                largura_amp = N_casos + altura_amp + altura_pontos
                if(largura_amp % 2 == 0): #verifica se é par
                    largura_amp = largura_amp + 1 #largura final da ampulheta
                else:
                    largura_amp = largura_amp + 2 #largura final da ampulheta

                #criação da matriz
                print('teste')
                matriz_ampulheta = [[0] * altura_amp, [0] * largura_amp]

                #contagem dos pontos de areia
                qtd_pontos = largura_amp - 6

                #atualizando altura da ampulheta
                altura_amp = altura_amp * 2

                #atribuição da ampulheta
                

                #impressão da ampulheta
                for ind_linha in range(altura_amp):
                    for ind_coluna in range(largura_amp):
                        print(matriz_ampulheta[ind_linha][ind_coluna], end = ' ')
                    print()

        cont_ampulheta = cont_ampulheta + 1 #vai para proxima ampulheta
