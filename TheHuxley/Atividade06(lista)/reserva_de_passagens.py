#37 -> 3
reserva = 0

num_voo = [0] * 37
qtd_assentos = [0] * 37

#dados dos voos
print('Digite o numero do voo e a quantidade de lugares disponiveis:')
for i in range(37):
    dados_voo = input().split()
    num_voo[i] = int(dados_voo[0])
    qtd_assentos[i] = int(dados_voo[1])

#reservas
while(reserva != 9999):
    print('Digite o pedido de reserva:')
    reserva = int(input())
    if(reserva == 9999):
        break
    else:
        for i in range(37):
            if(num_voo[i] == reserva):
                if(qtd_assentos[i] > 0):
                    print('Voo', num_voo[i], 'DISPONIVEL')
                    qtd_assentos[i] = qtd_assentos[i] - 1
                elif(qtd_assentos[i] == 0):
                    print('Voo', num_voo[i], 'INDISPONIVEL')
            elif(reserva not in num_voo):
                print('Voo', reserva, 'INDISPONIVEL')
                break
        
