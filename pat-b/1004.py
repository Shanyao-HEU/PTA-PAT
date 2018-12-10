#!/usr/bin/env python
# encoding: utf-8

'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

n = int(input())

stu_num_sco = []

def output_stu(stu):
    res = ''
    for item in stu[:2]:
        res = res + item +' '
    print(res[:-1])

for i in range(n):
    input_str = input()
    stu_num_sco.append([s for s in input_str.split()])

sort_stu_num_sco = sorted(stu_num_sco, key=lambda x: int(x[2]))
output_stu(sort_stu_num_sco[-1])
output_stu(sort_stu_num_sco[0])

