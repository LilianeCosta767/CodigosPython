#cont = 0 
valor = 0
Q = 0
genoma_inicial     = []
vetor_reverse_aux  = [0] * 2
vetor_reverse      = []

N = int(input())
if(N >= 1 and N <= 50000):
    R = int(input())
    if(R >= 0 and R <= 1000):
        for i in range(R):
            valor = input().split()
            vetor_reverse_aux[0] = valor[0]
            vetor_reverse_aux[1] = valor[1]
            #if(vetor_reverse_aux[0] <= 1 and 1 <= vetor_reverse_aux[1] and vetor_reverse_aux[1] <= N):
            vetor_reverse.append(vetor_reverse_aux[:])
        
        Q = int(input())

        # for i in range(N):
        #     valor = int(input())
        #     genoma_inicial.append(valor)

    print(vetor_reverse)