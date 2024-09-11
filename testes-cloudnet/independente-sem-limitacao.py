import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.027257089,
2.071337417,
3.010973129,
4.031679561,
4.994648946,
6.000204669,
6.978338102,
7.976593061,
8.96135777,
9.521329848
]
    fluxo_c2 = [1.027255626,
2.07133853,
3.010989588,
4.032178899,
4.99467963,
6.00037658,
6.978403209,
7.975981719,
8.961681829,
9.52099743
]
    fluxo_c3 = [1.02729138,
2.071341356,
3.010854036,
4.031338563,
4.994593406,
6.000030289,
6.97834109,
7.975769238,
8.961918613,
9.519128852
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.026893739,
2.071306461,
3.010923273,
4.029744522,
4.994567289,
5.99911171,
6.978280294,
7.975753443,
8.958490862,
9.516794469
]
    erros_maximos_c1 = [1.027305997,
2.071366682,
3.01101531,
4.032895605,
4.994756763,
6.002360987,
6.978419258,
7.978312983,
8.962208696,
9.527476959,
]
    
    erros_minimos_c2 = [1.026901303,
2.071315535,
3.010961047,
4.031529563,
4.994607072,
5.999149385,
6.978255976,
7.972640264,
8.958430232,
9.517533975
]
    erros_maximos_c2 = [1.027309475,
2.07136462,
3.011034498,
4.033437353,
4.994894029,
6.003312755,
6.978692338,
7.978141491,
8.962142662,
9.524016648
]
    
    erros_minimos_c3 = [1.02728288,
2.071319247,
3.009824063,
4.028190165,
4.993951722,
5.999098033,
6.978260839,
7.975576457,
8.960822176,
9.516289542
]
    erros_maximos_c3 = [1.027305485,
2.07136132,
3.011119646,
4.032962614,
4.994743832,
6.001441644,
6.978416478,
7.975889165,
8.962110537,
9.522898826
]
    
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

    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='best', fontsize=8)

    plt.tick_params(labelsize=8)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("independente-sem-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
