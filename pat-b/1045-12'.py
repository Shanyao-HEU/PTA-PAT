#!/usr/bin/env python
# encoding: utf-8
'''
@author: jiangsy
@eamil: jiangshanyao_heu@163.com
'''
N = int(input())
nums = [int(i) for i in input().split()]

ans = []
for i in range(N):
    n = nums[i]
    if i == 0:
        if min(nums[i+1:])>n:
            ans.append(n)
    elif i == N-1:
        if max(nums[:i])<n:
            ans.append(n)
    else:
        if max(nums[:i]) < n and min(nums[i+1:])>n:
            ans.append(n)

ans.sort()
print(len(ans))
res = ''
for a in ans:
    res = res + str(a) +' '
print(res[:-1])