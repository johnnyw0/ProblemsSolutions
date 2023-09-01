#João André Watanabe, Pedro Kroll, turma A1

#Definindo a função 
def letras_agrupadas(arquivo, a):

    #Definindo a variável do arquivo e a do alfabeto
    arq = open(arquivo, 'w')
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #Estrutura de repetição que faz uma partição no alfabeto do tamanho que o usuário desejar
    for i in range(0, len(alfabeto)-1, a):
        arq.write(alfabeto[i:i+a])
        arq.write('\n')
    arq.close()

letras_agrupadas('write.txt', 4)