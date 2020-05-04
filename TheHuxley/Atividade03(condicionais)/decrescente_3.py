#ordena 3 numeros inteiros em ordem decrescente
#ATIVIDADE DO THEHUXLEY

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 == n2 == n3):
    print('{}\n{}\n{}\n'.format(n3,n2,n1))
elif(n1 == n2):
    if(n2 > n3):
        print('{}\n{}\n{}\n'.format(n2,n1,n3))
    else: #n3 > n2
        print('{}\n{}\n{}\n'.format(n3,n2,n1))
elif(n2 == n3):
    if(n1 > n2):
        print('{}\n{}\n{}\n'.format(n1,n2,n3))
    else: #n2 > n1
        print('{}\n{}\n{}\n'.format(n3,n2,n1))
elif(n1 == n3):
    if(n2 > n1):
        print('{}\n{}\n{}\n'.format(n2,n1,n3))
    else: #n1 > n2
        print('{}\n{}\n{}\n'.format(n1,n3,n2))

elif(n1 > n2 and n1 > n3): #quando o primeiro numero é o maior
    if(n2 > n3):
        print('{}\n{}\n{}\n'.format(n1,n2,n3))
    else: #n3 > n2
        print('{}\n{}\n{}\n'.format(n1,n3,n2))
elif(n3 > n2 and n3 > n1): #uando o terceiro numero é o maior
    if(n1 > n2):
        print('{}\n{}\n{}\n'.format(n3,n1,n2))
    else: #n2 > n1
        print('{}\n{}\n{}\n'.format(n3,n2,n1))
elif(n2 > n1 and n2 > n3): #quando o segundo numero é o maior
    if(n1 > n3):
        print('{}\n{}\n{}\n'.format(n2,n1,n3))
    else: #n3 > n1
        print('{}\n{}\n{}\n'.format(n2,n3,n1))



# 1 1 1 OK
# 1 1 2 OK
# 2 2 1 OK
# 2 1 1 OK
# 1 2 2 OK
# 1 2 1 OK
# 2 1 2 OK
# 1 2 3 OK
# 3 2 1 OK
# 3 1 2 OK
# 2 1 3 || 1 2 3 OK
# 2 3 1 OK
# 1 3 2 OK
