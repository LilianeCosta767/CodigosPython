num1 = 0
num2 = 0
operador = ""

num1 = float(input())

while(operador != '&'):
    num2 = float(input())
    operador = input()
    if(operador == '+'):
        num1 = num1 + num2 #atualizando o valor de num1 para proxima conta
        print('{:.3f}'.format(num1))
        continue
    elif(operador == '-'):
        num1 = num1 - num2 #atualizando o valor de num1 para proxima conta
        print('{:.3f}'.format(num1))
        continue
    elif(operador == '*'):
        num1 = num1 * num2 #atualizando o valor de num1 para proxima conta
        print('{:.3f}'.format(num1))
        continue
    elif(operador == '/'):
        if (num2 == 0):
            print("operacao nao pode ser realizada")
        else:
            num1 = num1 / num2 #atualizando o valor de num1 para proxima conta
            print('{:.3f}'.format(num1))
            continue
    elif(operador == '&'):
        break
