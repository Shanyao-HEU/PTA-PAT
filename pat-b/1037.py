#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
def convert_knut(some_knut):
    f = 1
    if some_knut < 0:
        f = -1
        some_knut = -some_knut
    elif some_knut == 0:
        return '0.0.0'

    a = some_knut // (17*29)
    b = (some_knut - a*17*29) // 29
    c = some_knut - a*17*29 - b*29

    if f == 1:
        ans = "{}.{}.{}".format(a, b, c)
    else:
        ans = "-{}.{}.{}".format(a, b, c)

    return ans

P, A = [i for i in input().split()]
pa, pb, pc = [int(s) for s in P.split(".")]
aa, ab, ac = [int(s) for s in A.split(".")]

p_knut = pa*17*29 + pb*29 + pc
a_knut = aa*17*29 + ab*29 + ac

print(convert_knut(a_knut - p_knut))