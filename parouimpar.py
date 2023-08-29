t = 1
n = int(input())

while n != 0:
    print(f'Teste {t}') 
    j1 = input()
    j2 = input()
    for i in range(n):
        A, B = map(int, input().split())
        if (A + B) % 2 == 0:
            print(j1)
        else:
            print(j2)
    n = int(input())
    t += 1
    print()