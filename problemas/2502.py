while True:
    try:
        C, N = map(int, input().split())
        maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cripto1 = {}
        cripto2 = {}
        value = input()
        key = input()

        for i in range(len(value)):
            cripto1.update({key[i]:value[i]})

        for i in range(len(value)):
            cripto1.update({value[i]:key[i]})


        for i in range(N):
            frase = input()
            frase_final = ''
            for letra in frase:
                if letra.upper() in cripto1:
                    if letra in maiuscula:
                        frase_final += cripto1[letra.upper()]
                    else:    
                        min = cripto1[letra.upper()].lower()
                        frase_final += min      
                elif letra.upper() in cripto2:
                    if letra in maiuscula:
                        frase_final += cripto2[letra.upper()]
                    else:    
                        min = cripto2[letra.upper()].lower()
                        frase_final += min 
                else:
                    frase_final += letra


            print(frase_final)
        print()
    except:
        break