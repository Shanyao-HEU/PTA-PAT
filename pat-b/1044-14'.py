#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

def mar_to(alpha):

    if ' ' in alpha:
        s1, s2 = alpha.split(' ')
        num = (lst2.index(s1) + 1) * 13 + lst1.index(s2)+1
    else:
        if alpha in lst1:
            num = lst1.index(alpha) + 1
        else:
            num = (lst2.index(alpha) + 1)*13
    return num

def to_mar(num):
    if int(num) < 13:
        alpha = lst1[int(num)-1]
    elif int(num) == 13:
        alpha = 'tam'
    else:
        alpha2 = lst1[int(num) % 13 - 1]
        alpha1 = lst2[int(num) // 13 - 1]
        alpha = alpha1 + ' ' + alpha2

    return alpha

if __name__ == '__main__':

    lst1 = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
    lst2 = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
    N = int(input())
    for i in range(N):
        s = input()
        if s[0].isdigit():
            print(to_mar(s))
        else:
            print(mar_to(s))