L, C, M, N = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]

sat = [[None] * C for _ in range(L)]

sat[0][0] = matriz[0][0]

for i in range(1, C):
    sat[0][i] = sat[0][i-1] + matriz[0][i]

for i in range(1, L):
    sat[i][0] = sat[i-1][0] + matriz[i][0]
    for j in range(1, C):
        sat[i][j] = sat[i-1][j] + sat[i][j-1] - sat[i-1][j-1] + matriz[i][j]

def soma_lote(lin_final, lin_inicial, col_final, col_inicial):
    soma = sat[lin_final][col_final]
    if lin_inicial != 0:
        soma -= sat[lin_inicial - 1][col_final]
    if col_inicial != 0:
        soma -= sat[lin_final][col_inicial - 1]
    if lin_inicial != 0 and col_inicial != 0:
        soma += sat[lin_inicial - 1][col_inicial - 1]
    return soma

maior = -1 
for i in range(L - M + 1):
    for j in range(C - N + 1):
        soma = soma_lote(i+M-1, i, j+N-1, j)
        if soma > maior:
            maior = soma

print(maior)