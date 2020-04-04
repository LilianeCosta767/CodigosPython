valores = input().split()

n = int(valores[0]) #inicio
m = int(valores[1]) #fim
while(n <= m):
    if(n % 5 == 0):
        if(m - n < 5):
            print('{}'.format(n), end="")
        elif(n < m):
            print('{}|'.format(n), end="")
        else:
            print('{}'.format(n))
    n = n + 1
