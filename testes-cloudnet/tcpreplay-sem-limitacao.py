import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [0.995, 2, 2.995, 3.335, 3.335, 3.37, 3.345, 3.365, 3.33, 3.34]
    fluxo_c2 = [1, 1.995, 3, 3.375, 3.33, 3.3, 3.36, 3.373, 3.35, 3.365]
    fluxo_c3 = [1, 2, 3, 3.365, 3.355, 3.355, 3.38, 3.335, 3.365, 3.355]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [0.99, 1.99, 2.99, 3.16, 3.24, 3.18, 3.28, 3.32, 3.21, 3.18]
    erros_maximos_c1 = [1, 2, 3, 3.37, 3.44, 3.5, 3.57, 3.5, 3.45, 3.35]
    
    erros_minimos_c2 = [0.99, 1.99, 2.99, 3.29, 3.14, 3.28, 3.18, 3.24, 3.28, 3.29]
    erros_maximos_c2 = [1, 2, 3, 3.58, 3.39, 3.44, 3.39, 3.48, 3.53, 3.51]
    
    erros_minimos_c3 = [0.99, 1.99, 2.99, 3.16, 3.24, 3.18, 3.28, 3.16, 3.21, 3.18]
    erros_maximos_c3 = [1, 2, 3, 3.37, 3.44, 3.4, 3.57, 3.43, 3.45, 3.35]
    
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
        diferenca_minima = [abs(t - emin) for t, emin in zip(tempos, erros_minimos)]
        diferenca_maxima = [abs(emax - t) for t, emax in zip(tempos, erros_maximos)]
        
        # Plota os pontos com barras de erro definidas pelos valores mínimos e máximos
        line = plt.plot(banda_requisitada, tempos, linestyle=estilos_linha[i], color=cores[i])[0]
        handles.append(Line2D([], [], color=cores[i], marker=formas_pontos[i], markersize=10, linestyle=estilos_linha[i]))
        plt.errorbar(banda_requisitada, tempos, yerr=[diferenca_minima, diferenca_maxima], fmt=formas_pontos[i], linestyle=estilos_linha[i], color=cores[i], capsize=5, label=nomes_legenda[i], ecolor=cores[i])

    plt.ylabel("Throughput (Mb/s)", fontsize=9)
    plt.xlabel("Requested Bandwidth (Mb/s)", fontsize=9)
    plt.grid(linestyle='dotted', axis='y')

    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8])
    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='best', fontsize=8)

    plt.tick_params(labelsize=8)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("tcpreplay-sem-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
