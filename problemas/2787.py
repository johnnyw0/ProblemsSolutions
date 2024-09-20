l = int(input())
c = int(input())

if l % 2 == 0:
    if c % 2 == 0:
        print(1)
    elif c % 2 != 0:
        print(0)
elif l % 2 != 0:
    if c % 2 == 0:
        print(0)
    elif c % 2 != 0:
        print(1)