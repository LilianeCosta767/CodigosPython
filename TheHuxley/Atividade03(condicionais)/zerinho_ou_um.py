#programa para ver quem ganhou no zerinho ou um

A = int(input()) #Alice
B = int(input()) #Beto
C = int(input()) #Carla

if(A == 1 and B == 0 and C == 0):
    print('A\n')
elif(A == 0 and B == 1 and C == 0):
    print('B\n')
elif(A == 0 and B == 0 and C == 1):
    print('C\n')
elif(A == 0 and B == 1 and C == 1):
    print('A\n')
elif(A == 1 and B == 0 and C == 1):
    print('B\n')
elif(A == 1 and B == 1 and C == 0):
    print('C\n')
else:
    print('*\n')