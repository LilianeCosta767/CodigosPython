import math
import statistics

numero = 0
cont_numeros = 0 
vetor_numeros = []
media = 0
soma = 0
desvio_soma = 0
desvio_divid = 0
desvio_final = 0
qtd_media_maior = 0

# pegando os valores
while(numero != -1):
    numero = float(input())
    if(numero == -1):
        break
    else:
        vetor_numeros.append(numero)
        cont_numeros = cont_numeros + 1

# calculo da media
for i in range (cont_numeros):
    soma = soma + vetor_numeros[i]
media = soma / cont_numeros

# # calculo do desvio padrao
# for i in range (cont_numeros):
#     desvio_soma = desvio_soma + pow((vetor_numeros[i] - media), 2)
# desvio_divid = desvio_soma / cont_numeros
# desvio_final = math.sqrt(desvio_divid)

# calculando qtd de notas maiores que a media
for i in range (cont_numeros):
    if(vetor_numeros[i] > media):
        qtd_media_maior = qtd_media_maior + 1
qtd_media_maior = int(qtd_media_maior)

print('{:.2f}'.format(media))
#print('{:.2f}'.format(desvio_final))
print('{:.2f}'.format(statistics.stdev(vetor_numeros)))
print(qtd_media_maior)
