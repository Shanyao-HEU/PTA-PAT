s1, s2, K = input().split()
def convf(s):
    n, m = s.split('/')
    return int(n) / int(m)

s1 = convf(s1)
s2 = convf(s2)

left = int(min(s1, s2) * int(K))
right = int(max(s1, s2) * int(K))

def isyf(a, b):
    for i in range(2, min(a, b)):
        if a % i == 0 and b%i==0:
            return True
    return False

res = ''
print(left, right)
for i in range(left, right+1):
    if isyf(i, int(K)):
        continue
    else:
        res = res + str(i) + '/' + str(K) + ' '

print(res[:-1])
    