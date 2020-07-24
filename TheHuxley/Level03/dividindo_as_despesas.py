contador=0
clara = 0.0
diana = 0.0

while contador < 6:
    valor = float(input())
    nome = input().upper()

    if nome == 'CLARA':
        clara +=  valor
    if nome == 'DIANA':
        diana += valor

    contador += 1

if clara > diana:
     print('DIANA')
     soma = (clara - diana) / 2
     print('%0.2f '%soma)
elif diana > clara:
    print('CLARA')
    soma1 = diana -clara
    soma1 = soma1 / 2
    print('%0.2f'%soma1)
elif clara == diana:
    print('MORADORAS QUITES')