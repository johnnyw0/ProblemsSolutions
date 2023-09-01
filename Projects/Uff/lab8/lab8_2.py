#João André Watanabe, Pedro Kroll, turma A1

#Definindo a função
def palavra_repetida(arquivo):

    #Abrindo o arquivo
    arq = open(arquivo, 'r')

    #Usando readlines() para gerar uma lista com todas as strings do arquivo
    palavras = arq.readlines()

    #Estrutura para com contador para encontrar a palavra que mais aparece utilizando o método count()
    for palavra in palavras:
        freq = -1
        contador = palavras.count(palavra)
        if contador > freq:
            freq = palavra
    return freq

print(palavra_repetida('txt.txt'))