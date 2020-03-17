n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1+n2+n3)/3
if m > 7:
    print('Aprovado')
elif m >= 5:
    print('Recuperação')
else:
    print('Reprovado')