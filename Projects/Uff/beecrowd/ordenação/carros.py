n, m = map(int, input().split())
matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

matriz_ord = sorted(matriz, key=sum)

for i in range(3):
    print(matriz.index(matriz_ord[i])+1)