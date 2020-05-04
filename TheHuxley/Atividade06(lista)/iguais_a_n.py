array = [0] * 101
cont = 0

#pega os 101 valores informados
for i in range(101):
    array[i] = int(input())

#verificação
for i in range(100):
    if(array[100] == array[i]): 
        print(i)