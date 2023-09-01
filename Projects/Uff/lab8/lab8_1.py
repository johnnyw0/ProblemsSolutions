#João André Watanabe, Pedro Kroll, turma A1

#Definindo a função
def maior_palavra(arquivo):

    #Variável de arquivo
    arq = open(arquivo, "r")

    #Estrutura de repetição para encontrar a maior palavra usando 
    #len(string) junto de uma sentinela que a identifica
    for palavra in arq:
        maior = -1
        tamanho = len(palavra)
        if tamanho > maior:
            maior = palavra

    #Fechando o arquivo
    arq.close()
    return maior

print(maior_palavra('txt.txt'))