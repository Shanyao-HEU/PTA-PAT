#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
s_lst = "PATest"
dic = {}

S = input()
for s in s_lst:
    dic[s] = S.count(s)
print(dic)
while dic:
    ans = ''
    for s in s_lst:
        if s in dic:
            if dic[s] > 0:
                ans = ans + s
                dic[s] -= 1
            else:
                del dic[s]
        else:
            continue

print(ans)
