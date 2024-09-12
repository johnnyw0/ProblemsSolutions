import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.027252093,
2.071099969,
3.010759254,
4.031174086,
4.994392597,
5.999973703,
6.9783652,
7.975408238,
8.962771726,
9.51994849
]
    fluxo_c2 = [1.027250923,
2.07131356,
3.010672871,
4.031772561,
4.99468781,
5.999887893,
6.978401543,
7.976509267,
8.96134654,
9.519009206
]
    fluxo_c3 = [1.027227997,
2.071268461,
3.010742574,
4.031634985,
4.994450497,
5.999627767,
6.978053897,
7.97618463,
8.961314776,
9.519633268
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.026881884,
2.070512566,
3.009814776,
4.02820339,
4.991412993,
5.996756494,
6.978267787,
7.972655332,
8.961970441,
9.513705399
]
    erros_maximos_c1 = [1.027619501,
2.071377407,
3.011020107,
4.033793275,
4.994936801,
6.002792865,
6.978436628,
7.976737726,
8.967171207,
9.523186386
]
    
    erros_minimos_c2 = [1.026886176,
2.070510299,
3.009772538,
4.02975134,
4.992740423,
5.997716527,
6.978249028,
7.975772492,
8.958447173,
9.514452706
]
    erros_maximos_c2 = [1.027327989,
2.071855389,
3.01101591,
4.033412068,
4.996906136,
6.003156277,
6.978841047,
7.978182776,
8.962136415,
9.522194191
]
    
    erros_minimos_c3 = [1.026885052,
2.070545332,
3.009072339,
4.028196176,
4.992704147,
5.997583487,
6.975521618,
7.975040041,
8.958414183,
9.515559327
]
    erros_maximos_c3 = [1.027414433,
2.071409788,
3.011151127,
4.032917273,
4.994714988,
6.002027125,
6.978394938,
7.978081154,
8.962234575,
9.522984932
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
    fig.savefig("onos-independente-sem-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
