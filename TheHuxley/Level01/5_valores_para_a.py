cont = 0

for i in range(5):
    a = float(input("Digite um valor:\n"))
    if(a < 0):
        cont = cont + 1

print("Foram digitados", cont, "numeros negativos")