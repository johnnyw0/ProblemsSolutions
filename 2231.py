import sys
teste = 1
n, m = map(int, input().split())
while n != 0 and m != 0:
    
    temp = []

    for i in range(n):
        t = int(input())
        temp.append(t)

    temp_acumulada = [0] * n
    temp_acumulada[0] = temp[0]
    for i in range(1, n):
        temp_acumulada[i] += temp[i] + temp_acumulada[i-1]
    maior = -201
    menor = 201

    for i in range((n - m)+1):
        media = 0
        if i != 0:
            media += int((temp_acumulada[i+m-1] - temp_acumulada[i-1])/m)
        else:
            media += int(temp_acumulada[i+m-1]/m)
        if media > maior: maior = media
        if media < menor: menor = media
    print(f'Teste {teste}')
    print(menor, maior)
    print()
    teste += 1
    n, m = map(int, input().split())
