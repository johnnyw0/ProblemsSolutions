
N = int(input())
teste = 1

while N != 0: 
    senha = []
    L = list(input().split())
    
    mapeamento = [
        [L[0], L[1]],    #A
        [L[2], L[3]],    #B   
        [L[4], L[5]],    #C
        [L[6], L[7]],    #D
        [L[8], L[9]],    #E
    ]

    for letra in L[10:]:
            indice = ord(letra) - ord('A')
            senha.append(mapeamento[indice].copy())

    for i in range(N-1):
        L = list(input().split())
        mapeamento = [
        [L[0], L[1]],    #A
        [L[2], L[3]],    #B   
        [L[4], L[5]],    #C
        [L[6], L[7]],    #D
        [L[8], L[9]],    #E
    ]
        for j in range(6):
            indice = ord(L[j+10]) - ord('A')
            for digito in senha[j]:
                if digito not in mapeamento[indice]:
                    senha[j].remove(digito)
    
    print(f'Teste {teste}')
    print(f'{senha[0][0]} {senha[1][0]} {senha[2][0]} {senha[3][0]} {senha[4][0]} {senha[5][0]} ')
    print()
    
    N = int(input())
    teste += 1