t = 1

while True:
    P, R = map(int, input().split())
    if R == P == 0:
        break
    else:
        fila = list(map(int, input().split()))
        for i in range(R):
            N, O, *A = map(int, input().split())
            for j in range(N-1, -1, -1):
                if A[j] != O:
                  fila.pop(j)
    print(f'Teste {t}')
    for x in range(len(fila)):
        print(fila[x])
    t += 1
    print()