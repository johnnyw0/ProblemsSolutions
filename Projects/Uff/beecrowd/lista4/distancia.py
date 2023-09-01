n = int(input())
v = list(map(int, input().split()))

d1 = v[0]
maior = -1
for i in range(1, n):
    d1 += 1
    maior = max(maior, d1 + v[i])
    d1 = max(d1, v[i])

print(maior)