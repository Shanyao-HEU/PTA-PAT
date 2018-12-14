#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = input()
n1 = n
n1 = list(str(n1))
n1.sort(reverse=True)
a1 = int(''.join(n1))
n1.sort()
a2 = int(''.join(n1))
if a1 == a2:
    print("{} - {} = 0000".format(a1, a2))
else:
    while int(n) - 6174 != 0:

        n = list(str(n))

        n.sort(reverse=True)
        a1 = int(''.join(n))
        n.sort()
        a2 = int(''.join(n))
        n = a1 - a2
        while len(str(n)) < 4:
            n = '0'+str(n)
        print("{} - {:0>4d} = {:0>4d}".format(a1, a2, int(n)))

