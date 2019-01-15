#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''


s1 = input()
s2 = input()

dic1 = {}

for s in s1:
    if s not in dic1:
        dic1[s] = 1
    else:
        dic1[s] += 1

for s in s2:
    if s not in dic1:
        dic1[s] = -1
    else:
        dic1[s] -= 1


c1 = 0
c2 = 0
for k, v in dic1.items():
    if v < 0:
        c2 += (-v)
    else:
        c1 += v

if c2 != 0:
    print("No {}".format(c2))
else:
    print("Yes {}".format(c1))