lista = list(map(int, input().split()))

soma_acumulada = [lista[0]]

for i in range(len(lista)):
    soma_acumulada.append(soma_acumulada[i] + lista[i+1])

print(lista)
print(soma_acumulada)