#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''



def main():
    n_score = {}
    n = int(input())
    for i in range(n):
        num, s = [c for c in input().split()]
        if num in n_score:
            n_score[num] += int(s)
        else:
            n_score[num] = int(s)

    sort_n_score = sorted(n_score.items(), key=lambda x: x[1])
    print("{} {}".format(sort_n_score[-1][0], sort_n_score[-1][1]))

main()
