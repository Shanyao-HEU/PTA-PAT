import math
N = int(input())
dic1 = {}
for i in range(N):
    temp = input()
    dic1[temp] = i+1

K = int(input())

def isPrime(n):
    if n==2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True
    

lst1 = []
for i in range(K):
    inp = input()
    if inp not in dic1:
        print("{}: Are you kidding?".format(inp))
    else:
        if inp not in lst1:
            lst1.append(inp)

            mc = dic1[inp]
            if mc == 1:
                print("{}: Mystery Award".format(inp))
            elif isPrime(mc):
                print("{}: Minion".format(inp))
            else:
                print("{}: Chocolate".format(inp))
        else:
            print("{}: Checked".format(inp))
        