#João André Campos Watanabe, turma A1

#número final da tabela de multiplicação
n = int(input())


#loop (i) representa a primeira parte da multiplicação, enquanto o loop (j) representa a segunda parte
#ou seja, em i = 1: tabela = 1x1, 1x2, 1x3, 1x4, em i = n+1: tabela = nx1, nx2, ... , nxn 
for i in range(1, n+1):
    for j in range(1, n+1):
        resultado = i * j
        print(i, 'x', j, '=', resultado)

