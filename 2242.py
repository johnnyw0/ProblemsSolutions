def isvowel(string):
    vogal = 'aeiou'
    return vogal.find(string) != -1

teste1 = teste2 = ''

risada = input()
risada_inv = risada[::-1]

for letra in risada:
    if isvowel(letra):
        teste1 += letra
for letra in risada_inv:
    if isvowel(letra):
        teste2 += letra

if teste1 == teste2:
    print('S')
else:
    print('N')