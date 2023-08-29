def maior_palavra(arquivo):
    arq = open(arquivo, 'r')
    for palavra in arq:
        maior = -1
        tamanho = len(palavra)
        if tamanho > maior:
            maior = palavra
    arq.close()
    return maior

print(maior_palavra('txt.txt'))

