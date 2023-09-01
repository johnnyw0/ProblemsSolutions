import math as m

x1 = float(input('x do primeiro ponto: '))
y1 = float(input('y do primeiro ponto: '))
x2 = float(input('x do segundo ponto: '))
y2 = float(input('y do segundo ponto: '))

cateto1 = y2 - y1
cateto2 = x2 - x1

hip = m.sqrt(cateto1 ** 2 + cateto2 ** 2)
print(f'A distância entre os pontos é de aproximadamente {hip:.2f} unidades de distância.')