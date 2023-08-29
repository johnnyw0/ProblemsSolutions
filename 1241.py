n = int(input())
for i in range(n):
    a, b = input().split()
    index = a.find(b)
    if a[index:] == b:
        print('encaixa')
    else:
        print('nao encaixa')