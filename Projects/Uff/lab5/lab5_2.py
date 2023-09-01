#João André Campos Watanabe, turma A1

#Criando a lista a partir dos valores dados
linha = input('Entre com os elementos da lista: ')
valores = []
palavras = linha.split()
for i in range(len(palavras)):
    valores.append(palavras[i])

#Guardando elemento a ser adicionado e a sua posição
elemento = input('Entre com um elemento a ser inserido: ')
posição = int(input('Entre com a posição para inserir o elemento: '))

#Criando novas listas para adicionar o elemento no final da primeira e concatenando com os elementos restantes
lista1 = valores[:posição]
lista2 = valores[posição:]
lista1.append(elemento)
lista_final = lista1 + lista2
#Escrevendo a lista atualizada

print(lista_final)