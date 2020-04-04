valores = input().split()

n = int(valores[0]) #inicio
m = int(valores[1]) #fim
while(n <= m):
    if(n % 5 == 0):
        if(n < m):
            print('{}|'.format(n), end="")
        else:
            print('{}'.format(n), end="")
    n = n + 1

