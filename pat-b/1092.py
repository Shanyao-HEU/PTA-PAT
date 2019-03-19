n, m = map(int, input().split())
def addList(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c
 
nums = [0 for i in range(n)]
for i in range(m):
    temp = [int(t) for t in input().split()]
    nums = addList(nums, temp)
nums_dic = dict(zip(range(1,n+1), nums))
sort_nums_dic = sorted(nums_dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)

res = ''
max = sort_nums_dic[0][1]
print(max)
for a, b in sort_nums_dic:
    if b == max:
        res = res + str(a) + ' '
    else:
        break
print(res[:-1])