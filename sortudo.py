n, t = map(int, input().split())
partida = list(map(int, input().split()))
js = [0]*n

for i in range(n):
    for j in range(i, len(partida), n):
        js[i] += partida[j]

jso = sorted(js)
vencedor = js.index(jso[-1]) + 1 + js.count(jso[-1]) - 1    
print(vencedor)
