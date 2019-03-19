#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

import math
n = int(input())
m = [int(i) for i in input().split()]

m.sort(reverse=True)
num = math.sqrt(n)
if num % 1 == 0:
    x = y = int(num)
else:

    y = int(num) + 1
    while n % y != 0:
        y += 1
    x = n // y

rst = [[''] * x for i in range(y)]

left = 0
right = x
top = 0
bottom = y
lx = ly = 0

i = 0
while i < n:
    if i == n - 1:
        rst[ly][lx] = str(m[i])
        i += 1

    while lx < right - 1 and i < n:
        rst[ly][lx] = str(m[i])
        lx += 1
        i += 1

    while ly < bottom - 1 and i < n:
        rst[ly][lx] = str(m[i])
        ly += 1
        i += 1

    while left < lx and i < n:
        rst[ly][lx] = str(m[i])
        lx -= 1
        i += 1

    while top < ly and i < n:
        rst[ly][lx] = str(m[i])
        ly -= 1
        i += 1

    left += 1
    right -= 1
    top += 1
    bottom -= 1
    lx += 1
    ly += 1


for i in rst:
    print(' '.join(i))
