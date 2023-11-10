t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    presentes = list(map(int, input().split()))
    viag = 0
    saco = presentes[0]
    for j in range(1, len(presentes)+1):
        saco += presentes[j]
        if saco >= M:
            saco = presentes[j]
            viag +=1
    print(viag)