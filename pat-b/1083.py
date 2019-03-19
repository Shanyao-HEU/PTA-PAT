n = int(input())
nums = [int(i) for i in input().split()]

minus = {}
for i in range(n):
    temp = abs(i+1 - nums[i])
    if temp not in minus:
        minus[temp] = 1
    else:
        minus[temp] += 1
        
sort_minus = sorted(minus.items(), key=lambda x: x[0], reverse=True)
for k, v in sort_minus:
    if v != 1:
        print(k, v)