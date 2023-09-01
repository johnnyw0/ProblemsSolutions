#João André Campos Watanabe, turma A1


#Função para calcular o MDC entre dois números
def get_mdc(x, y):
    mdc = 1
    div = 2
    while div <= x:
        if x % div == 0 and y % div == 0:
            mdc = div
        div += 1
    return mdc

#Função para verificar se a tripla é pitagórica primitva
def eh_tripla_pitag_prim(lista):
    pitagorica = primitiva = False

    #Ordenando o vetor usando o método selection sort
    for i in range(len(lista)):
        pos = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[pos]:
                pos = j
        lista[i], lista[pos] = lista[pos], lista[i]
    
    #Verificando se é uma tripla pitagórica
    if lista[0]**2 + lista[1]**2 == lista[2]**2:
        pitagorica = True

    #Verificando se é primitiva
    if get_mdc(lista[0], lista[1]) == 1 and get_mdc(lista[0], lista[2]) == 1 and get_mdc(lista[1], lista[2]) == 1:
        primitiva = True    

    return primitiva and pitagorica

print(eh_tripla_pitag_prim([3, 4, 5]))

print(eh_tripla_pitag_prim([7, 12, 13]))

print(eh_tripla_pitag_prim([39, 15, 36]))

print(eh_tripla_pitag_prim([77, 36, 85]))