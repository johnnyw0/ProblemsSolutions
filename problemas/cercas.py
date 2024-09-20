n, h = map(int, input().split())
tam = list(map(int, input().split()))
total = 0
iguais = False
while not iguais:
    for i in range(len(tam)-1):
        movimentos = 0
        movimentos += h - tam[i]
        tam[i] += movimentos
        tam[i+1] += movimentos
        total += movimentos
    for tamanho in tam:
        if tam[0] != tamanho:
            iguais = False
        else:
            iguais = True
print(movimentos)

