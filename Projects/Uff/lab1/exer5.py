m100, m50, m25, m10, m5 = 100, 50, 25, 10, 5
q100 = q50 = q25 = q10 = q5 = 0

v = int(input('Valor em centavos: '))

while v >= 100:
    q100 = q100 + 1
    v = v - 100

while v >= 50:
    q50 = q50 + 1
    v = v - 50

while v >= 25:
    q25 = q25 + 1
    v = v - 25

while v >= 10:
    q10 = q10 + 1
    v = v - 10

while v >= 5:
    q5 = q5 + 1
    v = v - 5

print(f'Serão usadas: {q100} moeda(s) de 1 real, {q50} moeda(s) de 50 centavos, {q25} moeda(s) de 25 centavos, {q10} moeda(s) de 10 centavos, {q5} moeda(s) de 5 centavos e sobrarão {v} centavos.')