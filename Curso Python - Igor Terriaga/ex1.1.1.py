""" Faça um programa que leia três notas, calcule a média do aluno e por fim imprima sua situação, como segue: 
a. media = (nota1 + nota2 + nota3)/3
b. Situação:
i. Aprovado: media > 7
ii. Recuperação: media < 7 and media >= 5
iii. Reprovado: media < 5 """

nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
nota3 = float(input('3ª Nota: '))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print('Aprovado', 'com media:',media)
elif media < 7 and media >= 5:
    print('Recuperacao', 'com media:',media)
else:
    print('Reprovado', 'com media:',media)