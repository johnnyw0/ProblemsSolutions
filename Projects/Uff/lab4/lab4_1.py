suporte = "0123456789"
num = int(input('Entre com um número inteiro positivo: '))

if num == 0:
    resposta = "0"
else:
    resposta = ""

while num > 0:
    ch = num % 10
    resposta = suporte[ch] + resposta
    num //= 10
print('O número foi atribuído à variável do tipo “string” e tem o valor', resposta)
