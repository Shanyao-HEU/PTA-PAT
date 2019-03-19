a, b = [i for i in input().split()]

step = 1
char = '0123456789JQK'
res = ''

for s in b[::-1]:
    s1 = int(s)
    ind = step - 1
    try:
        s2 = int(a[::-1][ind])
    except:
        s2 = 0
    if step % 2 != 0:
        temp = (s1+s2) % 13
        temp = char[temp]
    else:
        temp = s1 - s2
        if temp < 0:
            temp += 10

    res += str(temp)
    step += 1
    
print(res[::-1])
        