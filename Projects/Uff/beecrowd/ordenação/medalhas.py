n = int(input())
matriz = [input() for _ in range(n)]

matriz_ord = sorted(matriz, key=lambda x: [(tuple(map(int, x.split()[1:])), -ord(x[0]))], reverse=True)

print()
print()
for x in matriz_ord:
    print(x)