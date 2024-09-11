n = int(input('digite um numero: '))
coord = set()

for i in range(n):
    coord.add(input())

if len(coord) == n:
    print('0')
else:
    print('1')


matriz = []

for i in range(3):
    linha = list(map(int, input().split()))
    matriz.append(linha)

print(matriz)


matriz = [list(map(int, input().split())) for _ in range(3)]

print(matriz)