#Aluno: João André Campos Watanabe, turma A1



a = int(input('Entre com o valor de A: '))     #armazenando os valores que serão comparados
b = int(input('Entre com o valor de B: '))
c = int(input('Entre com o valor de C: '))
d = int(input('Entre com o valor de D: '))


if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:    #verificando se os valores atendem às condições
    print('Valores aceitos')
else:
    print('Valores não aceitos')
