n = int(input())

for i in range(n):
    certo = 0
    m = int(input())
    fila = list(map(int, input().split()))
    fila_ord = sorted(fila, reverse=True)
    for j in range(len(fila_ord)):
        if fila[j] == fila_ord[j]:
            certo += 1
    print(certo)