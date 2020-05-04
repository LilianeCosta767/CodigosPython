#programa para saber se a entrada (inteira) é par ou impar, positiva ou negativa, ou nula

N = int(input())

if(N == 0):
    print('NULO')
elif(N % 2 == 0 and N > 0):
    print('POSITIVO PAR')
elif(N % 2 != 0 and N > 0):
    print('POSITIVO IMPAR')
elif(N % 2 == 0 and N < 0):
    print('NEGATIVO PAR')
elif(N % 2 != 0 and N < 0):
    print('NEGATIVO IMPAR')