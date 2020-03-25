
num = 1001
while(num>=1000 and num<=9999):
    num = int(input())
    if(num<1000 or num > 9999):
        break
    inteiro = int(num / 100)
    resto = int(num%100)
    resul = inteiro + resto
    
    resul = resul * resul
    if(resul == num):
        print('propriedade do 3025!')
    else:
        print('numero comum')
