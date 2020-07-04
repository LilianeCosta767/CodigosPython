seg = int(input())
min = 0
hr = 0
dia = 0

def saida():
    print(int(dia))
    print(int(hr))
    print(int(min))
    print(int(seg))

if(seg < 60):
    saida()
elif(seg >= 60 and seg < 3600):
    min = seg / 60
    seg = seg % 60
    saida()
elif(seg >= 3600 and seg < 86400):
    hr = seg / 3600
    seg = seg - (int(hr) * 3600)
    min = seg / 60
    seg = seg % 60
    saida()
elif(seg >= 86400):
    dia = seg / 86400
    seg = seg - (int(dia) * 86400)
    hr = seg / 3600
    seg = seg - (int(hr) * 3600)
    min = seg / 60
    seg = seg % 60
    saida()