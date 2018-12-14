#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n, l, h = [int(i) for i in input().split()]
num_df_cf = {}
for i in range(n):
    num, df, cf = [int(c) for c in input().split()]
    num_df_cf[str(num)] = [df, cf]

g1, g2, g3, g4 = {}, {}, {}, {}

for num, f in num_df_cf.items():
    if f[0] >= h and f[1] >= h:
        g1[num] = f[0] + f[1]
    elif f[0] >= h and f[1] >= l:
        g2[num] = f[0] + f[1]
    elif f[0] < h and f[0] >= f[1] and f[0]>l:
        g3[num] = f[0] + f[1]
    elif f[0] > l and f[1] > l:
        g4[num] = f[0] + f[1]

total = 0
for g in [g1, g2, g3, g4]:
    total += len(g)

def ranking(x):
    sum = -x[1][0] - x[1][1]
    a = -x[1][0]
    b = x[0]
    return sum, a, b
print(total)
for g in [g1, g2, g3, g4]:
    temp = sorted(g.items(), key=ranking, reverse=True)
    for k, v in temp:
        print(k, num_df_cf[k][0], num_df_cf[k][1])