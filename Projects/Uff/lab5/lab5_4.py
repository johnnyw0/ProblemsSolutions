#João André Campos Watanabe, turma A1

#Criando a lista a partir dos valores dados
linha = input('Entre com os elementos da lista: ')
valores = []
palavras = linha.split()
for i in range(len(palavras)):
    valores.append(palavras[i])

#Guardando elemento a ser encontrado
elemento = input('Entre com o elemento a ser encontrado: ')

#Estrutura de decisão, caso o número não esteja na lista, apontar sua posição como -1, caso esteja na lista, buscar sua posição a partir da igualdade com os valores da lista
if elemento not in valores:
    print('O elemento', elemento, 'está na posição -1')
else:
    for i in range(len(valores)):
        if elemento == valores[i]:
            print('O elemento', elemento, 'está na posição', i)