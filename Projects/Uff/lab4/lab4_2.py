frase = input('Entre com uma frase').split()
frase_final = ''

for palavra in frase:
    palavra = palavra[0].upper() + palavra[1:].lower()
    frase_final = frase_final + palavra + ' '

print(frase_final.strip())