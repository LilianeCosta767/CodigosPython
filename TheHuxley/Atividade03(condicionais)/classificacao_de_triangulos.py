# verificar qual tipo de triangulo dado 3 valores

ladoA = int(input())
ladoB = int(input())
ladoC = int(input())

if(ladoA == ladoB and ladoA == ladoC):
    print('equilatero\n')
elif(ladoA == ladoB and ladoB != ladoC):
    print('isosceles\n')
elif(ladoA == ladoC and ladoB != ladoC):
    print('isosceles\n')
elif(ladoB == ladoC and ladoB != ladoA):
    print('isosceles\n')
elif(ladoA != ladoB and ladoB != ladoC and ladoA != ladoC):
    print('escaleno')