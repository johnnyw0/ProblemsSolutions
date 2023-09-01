P = list(map(int, input().split()))
M = list(map(int, input().split()))
F = list(map(int, input().split()))
Q = list(map(int, input().split()))
B = list(map(int, input().split()))
K = int(input())

soma = []
for i in range(1, len(P)):
    for j in range(1, len(M)):
        for k in range(1, len(F)):
            for l in range(1, len(Q)):
                for m in range(1, len(B)):
                    soma.append(P[i] + M[j] + F[k] + Q[l] + B[m])

soma.sort(reverse=True)
soma_total = 0
for i in range(K):
    soma_total += soma[i]

print(soma_total)