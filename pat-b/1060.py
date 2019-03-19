N = int(input())
nums = [int(i) for i in input().split()]

nums.sort(reverse=True)
e = 0
for i in range(N):
    if nums[i] > e + 1:
        e += 1
print(e)