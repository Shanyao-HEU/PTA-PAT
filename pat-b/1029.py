#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

good = input()
bad = input()
list = []
for g in good:
    if g not in bad:
        list.append(g)
res = []
for l in list:
    res.append(l.upper())
result = ''
for s in res:
    if s not in result:
        result += s

print(''.join(result))