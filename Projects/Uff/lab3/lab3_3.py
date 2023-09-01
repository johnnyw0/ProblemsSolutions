#João André Campos Watanabe, turma A1

#variaveis de contagem
pos = 0
soma = 0

#guardando os valores, verificando os positivos e somando para fazer a média
for i in range(6):
    numero = float(input('Entre com um valor: '))
    if numero > 0:
        pos += 1
        soma += numero
media = soma / pos

#escrevendo os resultados
print(pos, 'valores positivos')
print(media)