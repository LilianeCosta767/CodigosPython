""" Escreva um programa que leia duas Strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posição de início. """

string1 = input('Entre com a primeira string: ')
string2 = input('Entre com a segunda string: ')

if string2 in string1:
    pos = string1.find(string2[0])
    print('Está dentro')
    print(pos)
else:
    print('Nao está contida!')