#progII  = 45 alunos
#progIII = 30 alunos

progii = [0] * 4
progiii = [0] * 3
contem = []

progii_s = input().split()
progiii_s = input().split()

#pega as matriculas da turma progII
for i in range(4):
    progii[i] = progii_s[i]

#pega as matriculas da turma progIII
for i in range(3):
    progiii[i] = progiii_s[i]

for i in range(4):
    if(progii[i] in progiii):
        contem.append(progii[i])

for i in range(len(contem)):
    print(contem[i], end = ' ')