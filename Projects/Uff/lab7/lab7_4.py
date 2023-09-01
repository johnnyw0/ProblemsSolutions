#João André Campos Watanabe, turma A1


def conf_assentos_juntos(matriz, n):
    #Contador de possíveis configurações
    config = 0
    #Estrutura de repetição que passa por cada linha da matriz
    for i in range(len(matriz)):
        #Estrutura de repetição que passa pela linha de acordo com o número de pessoas que sentarão juntas
        for j in range(len(matriz[i])-n+1):
            livre = True
            #Estrutura de repetição para verificar cada elemento dentro do intervalo e concluir se é possível que
            #as pessoas sentem juntas ou não
            for k in range(n):
                #Caso não seja possível, condição de incrementar o contador é mudada para falsa
                if matriz[i][j+k] != 0:
                    livre = False
            #Caso seja possível, incrementa o contador
            if livre:
                config += 1
    return config



#Testes
print(conf_assentos_juntos([
[1, 0, 1, 0, 1, 0, 1],
[0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1],
[0, 1, 1, 1, 1, 0, 0]
], 2))

print(conf_assentos_juntos ([
[1, 0, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 0, 0],
], 4))