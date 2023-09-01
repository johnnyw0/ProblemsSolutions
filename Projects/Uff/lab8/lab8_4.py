#João André Watanabe, Pedro Kroll, turma A1

#Função de ordenação com o método selection adaptado para ordenar a matriz
def select_sort(matriz):
    for i in range(len(matriz)):
        pos = i
        for j in range(i+1, len(matriz)):
            if matriz[j][1] > matriz[pos][1]:
                pos = j
        matriz[i], matriz[pos] = matriz[pos], matriz[i]
    return matriz

#Função para ler o arquivo de entrada e gerar a saída
def medalha(entrada, saida):
    #Definindo as variáveis dos arquivos
    arq_entrada = open(entrada, 'r')
    arq_saida = open(saida, 'w')

    #Estrutura para montar a matriz com o nome do time, quantidade de medalhas e a soma delas
    matriz = []
    for elemento in arq_entrada:
        linha = elemento.split()
        linha.append(int(linha[1]) + int(linha[2]) + int(linha[3]))
        matriz.append(linha)

    #Chamando a função de ordenar a matriz e escrevendo no arquivo de saída as listas ordenadas  
    matriz_ord = select_sort(matriz)
    for x in matriz_ord:
        arq_saida.write((f'{x[0]} {x[1]} {x[2]} {x[3]} {x[4]}'))
        arq_saida.write('\n')  

#Chamando a função com os arquivos txt
medalha('medalhas.txt', 'write.txt')
