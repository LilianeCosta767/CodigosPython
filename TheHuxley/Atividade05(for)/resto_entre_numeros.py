X = int(input())
Y = int(input())
aux = 0

if(Y < X):
    aux = X
    X = Y
    Y = aux

for i in range(X, Y):
    if(X % 5 == 2 or X % 5 == 3):
        print(i)
    X = X + 1