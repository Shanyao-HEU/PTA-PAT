#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def insertion(n, m):
    flag = 0
    for i in range(len(n) - 1):
        l = n[:i + 2]
        l.sort()
        rest = l + n[i+2:]
        if flag == 1:
            rest = [str(i) for i in rest]
            print("Insertion Sort")
            print(' '.join(rest))
            exit()
        if rest == m:
            flag = 1

def merge(n, m):
    n = [[i] for i in n]
    flag = 0
    while len(n) > 1:
        temp = []
        rest = []
        if len(n) % 2 == 0:
            for i in range(0, len(n), 2):
                s = n[i] + n[i + 1]
                s.sort()
                temp.append(s)
            n = temp

        else:
            for i in range(0, len(n)-1, 2):
                s = n[i] + n[i + 1]
                s.sort()
                temp.append(s)

            n = temp

        for i in n:
            rest += i
        if flag == 1:
            rest = [str(i) for i in rest]
            print("Merge Sort")
            print(" ".join(rest))
            exit()
        if rest == m:
            flag = 1

input()
n1 = [int(i) for i in input().split()]
n2 = n1[:]
m = [int(i) for i in input().split()]
insertion(n1, m)
merge(n2, m)

