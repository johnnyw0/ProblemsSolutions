#distancia entre os predios indice final - indice inicial
#distancia entre os andares = indice(i)[n]

n = int(input())
bairro = list(map(int, input().split()))

maior_d = -1
for i in range(len(bairro)):
    for j in range(len(bairro)):
        distancia = bairro[i] + (j - i) + bairro[j]
        if distancia > maior_d:
            maior_d = distancia
print(maior_d)