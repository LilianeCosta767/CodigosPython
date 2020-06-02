""" Escreva um programa que leia duas Strings e gere uma terceira com
os caracteres comuns às duas strings lidas. """

string1 = input('Enter the frist string: ')
string2 = input('Enter the second string: ')

string3 = ''

for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i]==string2[j]:
            string3 += string1[i]

print(string3)