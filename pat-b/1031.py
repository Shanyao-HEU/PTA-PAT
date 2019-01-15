#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

import re

def compute_m(num):
    weights = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    z_m = {0:'1', 1:'0', 2:"X", 3:"9", 4:"8", 5:"7",
           6:"6", 7:"5", 8:"4", 9:"3", 10:"2"}
    temp = 0
    for i, n in enumerate(num[:-1]):
        temp += weights[i] * int(n)
    z = temp % 11
    m = z_m[z]
    return m



def exam(num):
    flag = 0
    num_match = re.match('^\d{17}(.)', num)
    if num_match:
        if compute_m(num_match.group(0)) == num_match.group(1):
            flag = 1

    return flag

def main():
    n = int(input())
    flag = 1
    for i in range(n):
        num = input()
        if not exam(num):
            print(num)
            flag = 0
        else:
            continue
    if flag:
        print("All passed")
    return

main()


