while True:
    h1, d1, h2, d2 = map(int, input().split())


    if h1 == 0 and h2 == 0 and d1 == 0 and d2 == 0:
        break

    if h1 == 0: 
        h1 = 24
    if h2 == 0:
        h2 = 24


    if h1 >= h2 and d1 >= d2 or h1 > h2 and d1 < d2:
        print(abs((h1*60)-(h2*60) - (d1 - d2) +1440))
        

    else:
        print(abs((h1*60)-(h2*60) + (d1 - d2)))
        
        
