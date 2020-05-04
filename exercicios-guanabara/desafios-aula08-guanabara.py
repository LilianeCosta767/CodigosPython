import math #importação de módulo
import random
#import emoji
# uso da biblioteca

"""raiz com uso do sqrt
num = int(input('Informe um inteiro: '))
raiz = math.sqrt(num)
print("Resultado da raíz: ", math.ceil(raiz))
"""

""" exemplo que nao deu certo por causa do modulo emoji:
num = random.randint(1, 10)
print(num)

print(emoji.emojize('Olá, Mundo! :sunglasses:', use_aliases=True))
"""

"""Desafio 16:
num = float(input('Informe um float: '))
num_int = math.trunc(num)
print('A parte inteira  de {} é: {}.' .format(num, num_int))
"""

"""Desafio 17:
co = float(input('Informe o cateto oposto....: '))
ca = float(input('Informe o cateto adjacente.: '))
hip = math.sqrt((co*co)+(ca*ca))
print('O valor da hipotenusa é: ', hip)
"""

an = float(input("Digite o ângulo que você deseja: "))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Sen = {:.2f} \nCos = {:.2f} \nTan = {:.2f}' .format(sen, cos, tan))

"""Desafio 19:
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print('O aluno sorteado foi: ', sort)
"""

"""Desafio 20:
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
lista = [a1, a2, a3, a4]
seq = random.sample(lista, 4)
print('A ordem sorteada foi: ', seq)
"""