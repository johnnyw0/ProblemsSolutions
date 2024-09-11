L, C = map(int, input().split())

matriz = [list(map(int, input().split())) for _ in range(L)]


maior_linha = -1
soma_linha = 0
for i in range(L):
    soma_linha = sum(matriz[i])
    if soma_linha > maior_linha:
        maior_linha = soma_linha

maior_coluna = -1
for i in range(C):
    soma_coluna = 0
    for j in range(L):
        soma_coluna += matriz[j][i]
    if soma_coluna > maior_coluna:
        maior_coluna = soma_coluna
    
maior = maior_linha if maior_linha > maior_coluna else maior_coluna
print(maior)