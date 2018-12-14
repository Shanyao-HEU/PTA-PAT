#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n, d = [int(i) for i in input().split()]
kucun = [int(i) for i in input().split()]
price = [int(i) for i in input().split()]

danjia = {}
for i in range(n):
    danjia[i] = [kucun[i], price[i]/kucun[i]]

sort_danjia = sorted(danjia.items(), key=lambda x: x[1][1], reverse=True)

ret = 0


for i in range(n):
    temp = d - sort_danjia[i][1][0]
    if temp <= 0:
        ret = ret + d * sort_danjia[i][1][1]
        break
    else:
        ret = ret + sort_danjia[i][1][0] * sort_danjia[i][1][1]
        d = d - sort_danjia[i][1][0]

print("{:.2f}".format(ret))