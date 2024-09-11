import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [0.913, 0.914, 0.913, 0.914, 0.913, 0.914, 0.875, 0.733, 0.711, 0.709]
    fluxo_c2 = [1, 2, 2.73, 2.73, 2.73, 2.73, 2.13, 1.29, 1.16, 1.14]
    fluxo_c3 = [1, 2, 3, 4, 5, 6, 7, 8, 8.16, 8.15]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [0.912, 0.913, 0.913, 0.912, 0.913, 0.913, 0.874, 0.731, 0.706, 0.704]
    erros_maximos_c1 = [0.914, 0.918, 0.917, 0.917, 0.915, 0.914, 0.876, 0.736, 0.711, 0.709]
    
    erros_minimos_c2 = [0.99, 1.99, 2.72, 2.72, 2.71, 2.71, 2.13, 1.28, 1.14, 1.14]
    erros_maximos_c2 = [1, 2, 2.73, 2.73, 2.73, 2.73, 2.14, 1.31, 1.16, 1.16]
    
    erros_minimos_c3 = [0.99, 1.99, 2.99, 3.99, 4.99, 5.99, 6.99, 7.99, 8.13, 8.13]
    erros_maximos_c3 = [1, 2, 3, 4, 5, 6, 7, 8, 8.16, 8.16]
    
    fig = plt.figure(figsize=(6,4))
    ax = fig.gca()

    # Definindo cores para cada tipo de intenção
    cores = ['blue', 'green', 'red']
    
    # Definindo formas para os pontos de cada tipo de intenção
    formas_pontos = ['^', 's', 'o']

    estilos_linha = ['solid', 'dashed', 'dotted']
    
    # Definindo nomes para cada tipo de intenção
    nomes_legenda = ['C1->S1', 'C2->S2', 'C3->S3']

    # Plotando os pontos para cada tipo de intenção
    handles = []
    for i in range(3):
        tempos = [fluxo_c1, fluxo_c2, fluxo_c3][i]
        erros_minimos = [erros_minimos_c1, erros_minimos_c2, erros_minimos_c3][i]
        erros_maximos = [erros_maximos_c1, erros_maximos_c2, erros_maximos_c3][i]
        
        # Calcula a diferença entre os valores máximos e mínimos e os valores médios dos pontos de dados
        diferenca_minima = [t - emin for t, emin in zip(tempos, erros_minimos)]
        diferenca_maxima = [emax - t for t, emax in zip(tempos, erros_maximos)]
        
        # Plota os pontos com barras de erro definidas pelos valores mínimos e máximos
        line = plt.plot(banda_requisitada, tempos, linestyle=estilos_linha[i], color=cores[i])[0]
        handles.append(Line2D([], [], color=cores[i], marker=formas_pontos[i], markersize=10, linestyle=estilos_linha[i]))
        plt.errorbar(banda_requisitada, tempos, yerr=[diferenca_minima, diferenca_maxima], fmt=formas_pontos[i], linestyle=estilos_linha[i], color=cores[i], capsize=5, label=nomes_legenda[i], ecolor=cores[i])

    plt.ylabel("Vazão (Mb/s)", fontsize=15)
    plt.xlabel("Banda Requisitada", fontsize=15)
    plt.grid(linestyle='dotted', axis='y')

    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='upper left', fontsize=13)

    plt.tick_params(labelsize=14)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("teste.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
