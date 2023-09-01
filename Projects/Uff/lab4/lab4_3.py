str1, str2 = input('Entre com duas palavras: ').split()

letras_iguais = 0
strc1 = str1.lower()
strc2 = str2.lower()

if len(strc1) != len(strc2):
    print(str1, 'e', str2, 'não são anagramas')
else: 
    for letra in strc1:
        index = strc2.find(letra)
    if index != -1:
        letras_iguais += 1
    else:
        print('não são anagramas')
    if letras_iguais == len(strc1):
        print('são anagramas')




