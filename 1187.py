matriz = []
O = input()
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
        
soma = qtd = 0

for i in range(12):
    for j in range(12):
        if i < j and i < 12 - j - 1:
            soma += matriz[i][j]
            qtd += 1
            
med = soma/qtd


if O == "S":
    print(f"{soma:.1f}")
if O == "M":
    print(f"{med:.1f}")