import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [10, 31, 53, 74]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [1.0513297310252572,
4.09295553328742,
3.1667027670593884,
3.1946974393669936
]
    fluxo_c2 = [2.121277477786591,
2.1132499143012486,
3.1865678573239373,
3.191239137386892
]
    fluxo_c3 = [3.177275864550209,
3.1752499897143496,
3.1677496408133665,
3.132905555776525
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [1.0419328392333913,
4.05520925719092,
3.099195309723467,
3.114397096383923
]
    erros_maximos_c1 = [1.059886962947198,
4.132549902021414,
3.210494551440682,
3.210347058790188
]
    
    erros_minimos_c2 = [2.109895149794681,
2.0863042743202653,
3.103062931810324,
3.1050035349587084
]
    erros_maximos_c2 = [2.137689733866948,
2.1263138562569703,
3.210597136848724,
3.2244241285727497
]
    
    erros_minimos_c3 = [3.153422318339703,
3.147285392481978,
3.1045155467017373,
3.102514735985032
]
    erros_maximos_c3 = [3.209959778277881,
3.1946680398766816,
3.210080520953127,
3.212095410672448
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

    plt.ylabel("Vazão (Mb/s)", fontsize=14)
    plt.xlabel("Tempo", fontsize=15)
    plt.grid(linestyle='dotted', axis='y')

    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='best', fontsize=13)

    plt.tick_params(labelsize=12)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("dinamico-com-limitacao-ONOS.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
