#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

xs_zs = [int(i) for i in input().split()]

res = []

if xs_zs[-1] == 0:
    del xs_zs[-2:]
for i in range(len(xs_zs)//2):
    xs = xs_zs[2*i]
    zs = xs_zs[2*i+1]
    xs = xs*zs
    if xs == 0:
        continue
    else:
        zs = zs - 1
        res.append(xs)
        res.append(zs)

result = ''
for r in res:
    result = result + str(r) +' '

print(result[:-1])