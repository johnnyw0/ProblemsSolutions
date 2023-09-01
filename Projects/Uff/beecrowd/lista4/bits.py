I = J = K = L = 0

n = 1
t = 1
n = int(input())
while n != 0:
    I = n//50
    if I != 0:
        n -= 50*I
    J = n//10
    if J != 0:
        n -= 10*J
    K = n//5
    if K != 0:
        n -= 5*K
    L = n
    print(f'Teste {t}')
    print(I, J, K, L)
    print()
    t += 1
    n = int(input())