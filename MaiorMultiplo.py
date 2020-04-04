M = int(input())
N = int(input())

inicio = M
maior_multiplo = 0

while(inicio <= N):
    if(inicio % M == 0):
        if(inicio <= N):
            maior_multiplo = inicio
    inicio = inicio + 1 #atualização de M

if(maior_multiplo != 0):
    print('{}\n'.format(maior_multiplo))
else:
    print('sem multiplos menores que {}'.format(N))