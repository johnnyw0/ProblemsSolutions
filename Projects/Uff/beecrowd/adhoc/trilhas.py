n = int(input())
trilhas = []

for i in range(n):
    m, *h = list(map(int, input().split()))
    trilhas.append((i+1, m, h))
for trilha in trilhas:
    subida = 0
    for i in range(trilha[1]-1):
        if trilha[2][i+1] > trilha[2][i]:
            subida += trilha[2][i+1] - trilha[2][i]
     



