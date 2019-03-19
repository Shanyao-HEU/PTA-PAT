#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

from math import sin, cos
r1, p1, r2, p2 = [float(i) for i in input().split()]

r11 = r1 * cos(p1)
p11 = r1 * sin(p1)

r22 = r2 * cos(p2)
p22 = r2 * sin(p2)

r = r11 * r22 - p11 * p22
p = r11 * p22 + r22 * p11

if p > 0:
    print("{:.2f}+{:.2f}i".format(r, p))
elif p == 0:
    print("{:.2f}".format(r))
else:
    print("{:.2f}{:.2f}i".format(r, p))