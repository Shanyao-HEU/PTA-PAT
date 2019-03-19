N, M = [int(i) for i in input().split()]

def func(t,M):
    if int(t) >= 0 and int(t) <= M:
        return True
    else:
        return False
    
def score(inp, M):
    temp = [int(i) for i in inp.split() if func(i, M)]
    temp1 = temp[1:]
    g1 = (sum(temp1)-max(temp1)-min(temp1))/(len(temp1)-2)
    g = int(round(g1+temp[0])/2)
    return g

for i in range(N):
    print(score(input(), M))