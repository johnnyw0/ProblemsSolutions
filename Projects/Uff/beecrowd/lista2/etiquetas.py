R = int(input(), 16)
G = int(input(), 16)
B = int(input(), 16)

qG = (R//G)**2
qB = (G//B)**2 *qG

max = 1 + qG + qB

print(f'{max:0x}')