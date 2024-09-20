import sys
n = int(input())

menor = sys.maxsize 
ind_menor = None

for ind in range(1, n+1):
    m, *h = map(int, input().split())

    custo_ida = 0
    custo_volta = 0
    for i in range(m-1):
        if h[i] < h[i+1]:
            custo_ida += (h[i+1] - h[i])
        elif h[i] > h[i+1]:
            custo_volta += (h[i] - h[i+1])
    custo = min(custo_ida, custo_volta)

    if custo < menor:
        menor = custo
        ind_menor = ind

print(ind_menor)