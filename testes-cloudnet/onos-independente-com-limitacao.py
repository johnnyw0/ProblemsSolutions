import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.027201215,
1.029044451,
0.967222137,
0.968124186,
0.966582986,
0.967503417,
0.966070488,
0.971581598,
0.970194373,
0.968809678
]
    fluxo_c2 = [1.02717875,
2.066973179,
2.184078066,
1.986113044,
1.968422923,
1.970963715,
1.973864635,
1.968917878,
1.972343189,
1.969208614
]
    fluxo_c3 = [1.027266654,
2.071247311,
3.010924977,
4.031161217,
4.994281742,
5.99917986,
6.978385844,
7.975956225,
8.961722864,
9.51690873
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.026629811,
1.020794685,
0.955017016,
0.958244801,
0.957310857,
0.95038997,
0.957330969,
0.959467741,
0.958469015,
0.949241215
]
    erros_maximos_c1 = [1.027405941,
1.034599707,
0.982807387,
0.988489104,
0.976933797,
0.980987344,
0.979236122,
0.98730687,
0.978078827,
0.986171836
]
    
    erros_minimos_c2 = [1.026886074,
2.027862568,
2.175790274,
1.97502282,
1.960804813,
1.963092292,
1.965424343,
1.964221248,
1.968838528,
1.958492134
]
    erros_maximos_c2 = [1.027307224,
2.071979408,
2.2302546,
1.99181532,
1.975761432,
1.982668561,
1.979258856,
1.976921714,
1.978062111,
1.974617476
]
    
    erros_minimos_c3 = [1.026895375,
2.070541005,
3.009803393,
4.029756955,
4.992640046,
5.996752914,
6.977893309,
7.972687055,
8.958599642,
9.502321025
]
    erros_maximos_c3 = [1.027389368,
2.071580167,
3.011522963,
4.032202484,
4.99472394,
6.002343068,
6.978923743,
7.978123231,
8.962510326,
9.523606893
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
    fig.savefig("onos-independente-com-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
