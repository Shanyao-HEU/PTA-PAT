#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def partial(a, da):
    res = ''
    for i in a:
        if i == da:
            res += i
    if res:
        return int(res)
    else:
        return 0

a, da, b, db = input().split()
print(partial(a, da)+partial(b, db))