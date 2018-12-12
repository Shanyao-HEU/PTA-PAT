#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def func(num_list):

    r1, r2, r3, r4, r5 = [], [], [], [], []
    for n in range(len(num_list)):
        num = num_list[n]

        if num % 5 == 0:
            if num % 2 == 0:
                r1.append(num)

        elif num % 5 == 1:
            r2.append(num)

        elif num % 5 == 2:
            r3.append(num)

        elif num % 5 == 3:
            r4.append(num)

        else:
            r5.append(num)
    if r1:
        r1 = sum(r1)
    else:
        r1 = 'N'

    if r2:
        r22 = 0
        for i in range(len(r2)):
            if i%2 == 0:
                r22 += r2[i]
            else:
                r22 -= r2[i]
    else:
        r22 = 'N'

    if r3:
        r3 = len(r3)
    else:
        r3 = 'N'

    if r4:
        r4 = round(sum(r4)/len(r4), 1)
    else:
        r4 = 'N'

    if r5:
        r5 = max(r5)
    else:
        r5 = 'N'

    res = ''
    for ans in [r1, r22, r3, r4, r5]:

        res = res + str(ans) +' '


    print(res[:-1])

num_list = [int(i) for i in input().split()][1:]
func(num_list)