n = int(input())
lista = list(map(int, input().split()))

soma = sum(lista)

if (soma - ((n*(n+1))/2)) % n != 0:
    print(-1)
else:
    base = (soma - ((n*(n+1))/2)) // n
    dif = 0
    for i in range(len(lista)):
        if lista[i] > base + i + 1:
            dif += lista[i] - (base + i + 1)
    print(int(dif))
