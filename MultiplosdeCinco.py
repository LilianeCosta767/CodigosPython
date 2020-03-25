valores = input().split()

n = int(valores[0]) #inicio
m = int(valores[1]) #fim
while(n <= m):
    if(n % 5 == 0):
        if(n < m):
            print(n, '|', end="")
        else:
            print(n, end="")
    n = n + 1

