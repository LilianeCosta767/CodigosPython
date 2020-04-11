altura_amp = 1
ind_vet = 0
cont_atribuicao = 0 #contador da coluna
largura_amp = 11

matriz = [[0] * altura_amp, [0] * largura_amp]

print(matriz)


# vet_ampulheta = colunas_amp + linhas_amp



# while(cont_atribuicao <= largura_amp): #percorre as colunas
#     if(cont_atribuicao == 0 or cont_atribuicao == 1):
#         vet_ampulheta[ind_vet][cont_atribuicao] = '*'
#     elif(cont_atribuicao == largura_amp or cont_atribuicao == (largura_amp - 1)):
#         vet_ampulheta[ind_vet][cont_atribuicao] = '*'
#     elif(vet_ampulheta[ind_vet-1] == '*'):
#         vet_ampulheta[ind_vet][cont_atribuicao] = ' *'
#     cont_atribuicao = cont_atribuicao + 1

# for ind_vet in range(len(altura_amp)):
#     print(vet_ampulheta)