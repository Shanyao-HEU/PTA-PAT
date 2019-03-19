N = int(input())
nums = [int(n) for n in input().split()]
res = 0
for i in range(N):
    res = res + nums[i] * 10 * (N-1) + sum(nums) - nums[i]
print(res)