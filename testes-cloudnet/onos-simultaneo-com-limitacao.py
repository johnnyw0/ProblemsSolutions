import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plotar_grafico():
    banda_requisitada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Valores de tempos para cada tipo de intenção
    fluxo_c1 = [0.988241796,
1.006639291,
0.999338278,
0.972290911,
0.999746098,
0.974191332,
0.98742601,
0.987222123,
0.986098928,
0.987552355
]
    fluxo_c2 = [1.005324103,
2.043166758,
3.006952794,
3.52917214,
2.99716968,
2.992133893,
2.98709212,
2.97395839,
3.00249271,
2.981275775
]
    fluxo_c3 = [1.004000957,
2.038271364,
3.075749422,
4.028455506,
4.950553763,
5.945690922,
6.504290053,
6.522749101,
6.496539836,
6.516751298
]

    # Valores de erros mínimos e máximos para cada tipo de intenção
    erros_minimos_c1 = [0.947614126,
0.970059307,
0.973016299,
0.95223006,
0.966961971,
0.954187763,
0.940752727,
0.955182137,
0.951255516,
0.959857764
]
    erros_maximos_c1 = [1.006270192,
1.161146303,
1.012448054,
0.993255551,
1.015134503,
1.001941652,
1.014088546,
1.016756823,
1.015061012,
1.023968683
]
    
    erros_minimos_c2 = [1.001330322,
2.032409203,
2.977985338,
3.508510822,
2.936304075,
2.914597424,
2.94095918,
2.906351897,
2.915939554,
2.932857544
]
    erros_maximos_c2 = [1.006725738,
2.045954807,
3.033825543,
3.551260798,
3.042392956,
3.072285417,
3.040112998,
3.063760083,
3.061427026,
3.049601642
]
    
    erros_minimos_c3 = [1.000380069,
2.031460805,
3.066729602,
3.96597983,
4.931355344,
5.915572001,
6.441241626,
6.464396769,
6.429870516,
6.432820565
]
    erros_maximos_c3 = [1.006261812,
2.046046907,
3.082335812,
4.045486918,
4.968702112,
5.977317282,
6.556428393,
6.585305369,
6.550987551,
6.566877869
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
    plt.xlabel("Banda Requisitada (Mb/s)", fontsize=15)
    plt.grid(linestyle='dotted', axis='y')
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # Criando os elementos personalizados da legenda
    plt.legend(handles, nomes_legenda, loc='upper left', fontsize=13)

    plt.tick_params(labelsize=12)
    plt.subplots_adjust(left=0.2, bottom=0.18, right=0.9, top=0.888, wspace=0.2, hspace=0.2)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(2)
    
    plt.show()
    fig.savefig("onos-simultaneo-com-limitacao.pdf", bbox_inches='tight')

if __name__ == "__main__":
    plotar_grafico()
