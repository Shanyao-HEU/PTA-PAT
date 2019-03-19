#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

N, e, D = input().split()

def func(e, D, temp):
    e = float(e)
    D = int(D)
    K = int(temp[0])
    flag = 0
    t_lst = [float(t) for t in temp[1:] if float(t) < e]
    if len(t_lst) > (K//2):
        flag = 1
        if K > D:
            flag = 2
    return flag

may_kz, kz = 0, 0
for i in range(int(N)):
    temp = [t for t in input().split()]
    if func(e, D, temp) == 1:
        may_kz += 1
    elif func(e, D, temp) == 2:
        kz += 1

print("{:.1f}% {:.1f}%".format(may_kz*100/int(N), kz*100/int(N)))

