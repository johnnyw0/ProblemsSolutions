import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [0.953272813,
0.953387657,
0.953355306,
0.953390613,
0.953391362,
0.953350087,
0.953397124,
0.953396077,
0.953392692,
0.953394757
]
    fluxo_c2 = [1.044026847,
1.998801925,
2.85760209,
2.857764362,
2.857974335,
2.857876093,
2.857811297,
2.857881977,
2.857982905,
2.858026775
]
    fluxo_c3 = [1.044077036,
2.026682551,
3.027728447,
4.009554914,
5.011433121,
5.989367909,
6.989873614,
7.969154486,
8.570758665,
8.570450341
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [0.952801774,
0.953284369,
0.953017126,
0.953373997,
0.953384326,
0.953034002,
0.953387627,
0.953386873,
0.953370369,
0.953378856
]
    erros_maximos_c1 = [0.953347785,
0.953409224,
0.95341866,
0.953414316,
0.953407432,
0.953411677,
0.953415072,
0.953407621,
0.953417713,
0.95340847
]
    
    erros_minimos_c2 = [1.043626081,
1.998338511,
2.85679862,
2.856846544,
2.857952998,
2.856829817,
2.856846544,
2.856825238,
2.857949025,
2.857950728
]
    erros_maximos_c2 = [1.044370529,
1.999084104,
2.858012526,
2.858019395,
2.858006626,
2.858169226,
2.858024219,
2.858064539,
2.858039826,
2.858250107
]
    
    erros_minimos_c3 = [1.044029461,
2.024684342,
3.026495756,
4.009467527,
5.011377336,
5.987196862,
6.989827854,
7.96604329,
8.569217937,
8.567466612
]
    erros_maximos_c3 = [1.044303233,
2.028757209,
3.028682376,
4.009667967,
5.011502081,
5.989681165,
6.989943298,
7.969779397,
8.571768498,
8.57311712
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
    fig.savefig("independente-com-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
