#João André Campos Watanabe, turma A1

#Guardando os valores da lista e o número que será contado
linha = input('Entre com uma lista: ')
E = input('Entre com um elemento para se verificar o número de vezes que ele aparece na lista: ')
contador = []

#Criando a lista a partir dos valores dados
valores = []
palavras = linha.split()
for i in range(len(palavras)):
    valores.append(palavras[i])

#Adicionando o elemento contado em outra lista de acordo com a quantidade de vezes que ele aparece
for elemento in valores:
    if elemento == E:
        contador.append(elemento)
        
#O número de vezes que o elemento aparece é representado pelo tamanho dessa nova lista
vezes = len(contador)
print('O elemento', E, 'aparece', vezes, 'vezes na lista.')

