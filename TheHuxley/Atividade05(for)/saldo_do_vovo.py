valores = input().split()

N = int(valores[0]) #numero de dias
S = int(valores[1]) #valor do saldo

valor_op = 0 #valor de saque ou deposito
menor = 1000000000 #valor do menor Saldo da conta

for x in range(0,N):
    valor_op = int(input())
    S = S + valor_op
    if(S < menor): #atualizando o valor de menor
        menor = S

print(menor)