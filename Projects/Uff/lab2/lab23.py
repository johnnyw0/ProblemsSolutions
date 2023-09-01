#Aluno: João André Campos Watanabe, turma A1
import math

xa = float(input('Entre com a coordenada x do ponto A: '))      #armazenando as coodernadas dos vértices do triângulo
ya = float(input('Entre com a coordenada y do ponto A: '))
xb = float(input('Entre com a coordenada x do ponto B: '))
yb = float(input('Entre com a coordenada y do ponto B: '))
xc = float(input('Entre com a coordenada x do ponto C: '))
yc = float(input('Entre com a coordenada y do ponto C: '))


l1 = math.sqrt((yb - ya) ** 2 + (xb - xa) ** 2)           #descobrindo a medida dos lados a partir do teorema de Pitágoras
l2 = math.sqrt((yb - yc) ** 2 + (xb - xc) ** 2)
l3 = math.sqrt((yc - ya) ** 2 + (xc - xa) ** 2)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:       #verificando se é triângulo a partir da condição de existência e testando a sua classificação a partir da relação entre os lados 
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l1 == l2 or l2 == l3:
        print('Isósceles')
    else:
        print('Escaleno')
else: 
    print('Não é triângulo')
    
    


