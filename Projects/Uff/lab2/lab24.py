#Aluno: João André Campos Watanabe, turma A1

num = int(input('Entre com um número inteiro de 5 dígitos: '))     #armazenando o número em que será feita a verificação de palíndromo 



if num // 10000 == num % 10 and (num // 1000) % 10 == (num % 100) // 10:   #verificando a igualdade do primeiro com o último e do segundo com o penúltimo número a partir de operações com módulo e divisão inteira 
    print('O número é palíndromo')

else:
    print('O número não é palíndromo')

