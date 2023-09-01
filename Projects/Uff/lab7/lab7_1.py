#João André Campos Watanabe, turma A1

def kempner(num):

    #Inicializando variáveis de multiplicação como 1
    fat = 1
    indice = 1

    #Estrutura de repetição que calcula o fatorial dos números a partir de 1 
    #até encontrar o índice daquele que é divido pelo número
    while fat % num != 0:
        fat *= indice
        indice += 1
    return indice-1

#Testes
print(f'kempner(6) ==> {kempner(6)}')
print()
print(f'kempner(10) ==> {kempner(10)}')