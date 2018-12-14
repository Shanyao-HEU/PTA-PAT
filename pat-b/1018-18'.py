#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''

record = {"2":0, "1":0, "0":0 }
win1 = {"C":0, "J":0, "B":0}
win2 = {"C":0, "J":0, "B":0}
n = int(input())
for i in range(n):
    s1, s2 = input().split()
    if s1 == 'C':
        if s2 == 'C':
            record['1'] += 1
        elif s2 == 'J':
            record['2'] += 1
            win1['C'] += 1
        else:
            record['0'] += 1
            win2['B'] += 1

    elif s1 == "J":
        if s2 == "C":
            record['0'] += 1
            win2['C'] += 1
        elif s2 == "J":
            record['1'] += 1
        else:
            record['2'] += 1
            win1['J'] += 1
    else:
        if s2 == "C":
            record['2'] += 1
            win1['B'] += 1
        elif s2 == "J":
            record['0'] += 1
            win2['J'] += 1
        else:
            record['1'] += 1

print(record["2"], record["1"], record["0"])
print(record["0"], record["1"], record["2"])

def ranking(x):
    return x[1], -ord(x[0])

lst1 = sorted(win1.items(), key=ranking)
lst2 = sorted(win2.items(), key=ranking)

print(lst1[-1][0], lst2[-1][0])