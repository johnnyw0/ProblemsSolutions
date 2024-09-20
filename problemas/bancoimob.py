q, n = map(int, input().split())
V = [q]*3

for i in range(n):
    o, *j = input().split()
    if o == 'C':
        V[ord(j[0]) - ord('D')] -= int(j[1])
    elif o == 'V':
        V[ord(j[0]) - ord('D')] += int(j[1])
    else:
        V[ord(j[0]) - ord('D')] += int(j[2])
        V[ord(j[1]) - ord('D')] -= int(j[2])
        
print(f'{V[0]} {V[1]} {V[2]}')