from functools import reduce
N = int(input())
nums = [int(i) for i in input().split()]

nums.sort()

print(int(reduce(lambda x, y:(x+y)/2, nums)))

