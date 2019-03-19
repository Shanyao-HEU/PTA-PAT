#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def func(i, s1, s2):
    if i % 2 != 0:
        ans = (int(s1) + int(s2)) % 13
        if ans == 10:
            ans = 'J'
        elif ans == 11:
            ans = 'Q'
        elif ans == 12:
            ans = 'K'
    else:
        ans = int(s2) - int(s1)
        if ans < 0:
            ans += 10
    return str(ans)

n1, n2 = input().split()
n1 = n1[::-1]
n2 = n2[::-1]
print(n1, n2)
res = ''
for i in range(len(n2)-1, -1, -1):

    if i >= len(n1):
        temp = n2[i]
    else:
        temp = func(i+1, n2[i], n1[i])
    res += temp

print(res)

