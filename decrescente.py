#ordena 3 numeros inteiros em ordem decrescente
#ATIVIDADE DO THEHUXLEY

n1 = int(input())
n2 = int(input())
n3 = int(input())

# 1 2 1

if(n1 == n2 and n1 == n3):
    print('{}\n{}\n{}\n'.format(n1,n2,n3))
elif(n1 > n2 and n1 > n3):
    if(n2 > n3):
        print('{}\n{}\n{}\n'.format(n1,n2,n3))
    elif(n3 > n2):
        print('{}\n{}\n{}\n'.format(n1,n3,n2))
    elif(n3 == n2):
        print('{}\n{}\n{}\n'.format(n1,n2,n3))
elif(n2 > n1 and n2 > n3):
    if(n1 > n3):
        print('{}\n{}\n{}\n'.format(n2,n1,n3))
    elif(n3 > n1):
        print('{}\n{}\n{}\n'.format(n2,n3,n1))
    elif(n1 == n3):
        print('{}\n{}\n{}\n'.format(n2,n1,n3))
elif(n3 > n1 and n3 > n2):
    if(n2 > n1):
        print('{}\n{}\n{}\n'.format(n3,n2,n1))
    elif(n1 > n2):
        print('{}\n{}\n{}\n'.format(n3,n1,n2))
    elif(n1 == n2):
        print('{}\n{}\n{}\n'.format(n3,n1,n2))
