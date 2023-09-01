#João André Campos Watanabe, turma A1

def tabuleiro_xadrez(n, e1, e2):

    #Inicializando o tabuleiro como vazio e mapeando o caso em que os dois elementos são iguais
    tabuleiro = []
    if e1 == e2:
        return "Inválido"
    
    #Estrutura de repetição que cria listas com os valores alternados 
    #baseando-se no índice e as insere no tabuleiro
    else:
        for i in range(n):
            linha = []
            for j in range(n):
                if i % 2 == 0:
                    if j % 2 == 0:
                        linha.append(e1)
                    else:
                        linha.append(e2)
                else:
                    if j % 2 == 0:
                        linha.append(e2)
                    else:
                        linha.append(e1)
            tabuleiro.append(linha)

    for lin in tabuleiro:
        print(lin)

#Testes
tabuleiro_xadrez(2, 7, 6)
print()
tabuleiro_xadrez(3, 'A', 'B')
print()
tabuleiro_xadrez(4, 'c', 'd')