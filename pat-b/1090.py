n, m = map(int, input().split())
dangers = []
for i in range(n):
    danger = (input().split())
    dangers.append(danger)

def isDanger(dangers, temp):
    
    for a, b in dangers:
        if a in temp:
            if b in temp:
                return "No"
            else:
                continue
        elif b in temp:
            if a in temp:
                return "No"
            else:
                continue
        else:
            continue
    return "Yes"
    
for i in range(m):
    temp = [i for i in input().split()]
    print(isDanger(dangers, temp))
        