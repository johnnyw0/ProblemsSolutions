import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [10, 31, 53, 74]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.905655136,
1.90574363,
4.442839409,
2.857978973
]
    fluxo_c2 = [0.953390445,
3.804147871,
2.815385171,
0.954973371
]
    fluxo_c3 = [2.857176632,
2.853921575,
2.263295875,
5.714486652
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.905147774,
1.904951542,
4.290748277,
2.856826698
]
    erros_maximos_c1 = [1.905741722,
1.906852428,
4.544348353,
2.858759055
]
    
    erros_minimos_c2 = [0.953022882,
3.802401478,
2.669040659,
0.953935033
]
    erros_maximos_c2 = [0.953722356,
3.807167634,
3.049565691,
0.956649881
]
    
    erros_minimos_c3 = [2.856110255,
2.851572297,
2.171673113,
5.71260673
]
    erros_maximos_c3 = [2.857533403,
2.856721516,
2.336590577,
5.716482231
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

    plt.ylabel("Vazão (Mb/s)", fontsize=9)
    plt.xlabel("Tempo", fontsize=9)
    plt.grid(linestyle='dotted', axis='y')
    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8])
    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='best', fontsize=8)

    plt.tick_params(labelsize=8)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("dinamico-com-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
