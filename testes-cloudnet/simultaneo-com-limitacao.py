import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [0.920757675,
0.882734617,
0.855883005,
0.828789346,
0.802146104,
0.763514038,
0.739138619,
0.686893368,
0.484149036,
0.48537939
]
    fluxo_c2 = [1.036129594,
1.985687177,
2.075818671,
1.867671993,
1.602766239,
1.361292216,
1.117930959,
0.839114117,
0.483952629,
0.483989633
]
    fluxo_c3 = [1.036141073,
2.078846238,
3.10187794,
4.003975136,
4.989764865,
6.009651486,
6.962512731,
7.937606659,
8.534827998,
8.535517931
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [0.912603203,
0.877394431,
0.84365819,
0.820441507,
0.790905212,
0.75117418,
0.720063501,
0.674342747,
0.481992424,
0.481862714
]
    erros_maximos_c1 = [0.944061872,
0.893106457,
0.86785354,
0.838726375,
0.813326317,
0.775655744,
0.75550815,
0.699373672,
0.492181129,
0.492323312
]
    
    erros_minimos_c2 = [1.006235873,
1.981432801,
2.062209717,
1.855311682,
1.587035705,
1.345262688,
1.100378175,
0.832100122,
0.482213644,
0.482752508
]
    erros_maximos_c2 = [1.039688328,
2.002799318,
2.091311423,
1.878395302,
1.615871225,
1.37681056,
1.145823505,
0.845342927,
0.484603374,
0.485294873
]
    
    erros_minimos_c3 = [1.006325467,
2.077487336,
3.082884816,
3.998399385,
4.985884653,
5.996016206,
6.953525907,
7.931992853,
8.529365783,
8.529178661
]
    erros_maximos_c3 = [1.039834115,
2.079138345,
3.106327333,
4.007240572,
4.992253284,
6.014102218,
6.968692207,
7.941437429,
8.536562637,
8.538501762
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
    fig.savefig("simultaneo-com-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
