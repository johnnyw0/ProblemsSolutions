import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.004504476,
2.04491539,
2.985297087,
3.164849854,
3.155222104,
3.145481774,
3.15069287,
3.160144789,
3.159958391,
3.175733661
]
    fluxo_c2 = [1.004389507,
2.042580827,
2.991826573,
3.172267455,
3.168266734,
3.168432931,
3.183663509,
3.17480436,
3.17001,
3.123539502
]
    fluxo_c3 = [1.004702418,
2.039240862,
2.975570848,
3.148585263,
3.165233406,
3.170057989,
3.149061751,
3.150769777,
3.154180555,
3.194139962
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.00037435,
2.037242543,
2.965609042,
3.096811138,
3.101253631,
3.095219254,
3.098696273,
3.097892912,
3.106591263,
3.097646598
]
    erros_maximos_c1 = [1.006384339,
2.045826611,
3.023475244,
3.200296163,
3.205125566,
3.19718136,
3.195955928,
3.190752311,
3.195713679,
3.200839904
]
    
    erros_minimos_c2 = [0.999744286,
2.03711262,
2.959565029,
3.104085925,
3.101538179,
3.097323753,
3.115880344,
3.107884856,
3.08575089,
3.100091453
]
    erros_maximos_c2 = [1.006534846,
2.046058268,
3.019040834,
3.195691743,
3.196624804,
3.195906627,
3.205145911,
3.196410455,
3.196093727,
3.199046069
]
    
    erros_minimos_c3 = [1.000819243,
2.03199332,
2.960991454,
3.096740108,
3.106212839,
3.096900542,
3.101237075,
3.097897201,
3.097922938,
3.184421251
]
    erros_maximos_c3 = [1.006248244,
2.045838375,
2.997719368,
3.196219525,
3.195231102,
3.195926853,
3.20988925,
3.195967306,
3.196376946,
3.209882902
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
    fig.savefig("onos-simultaneo-sem-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
