n = int(input())

def isZishou(k):
    dic = {}
    l = len(str(k))
    for i in range(1, 11):
        #print(str(i * k**2)[-l:])
        num = str(i * k**2)
        if num[-l:] == str(k):
            dic[i] = num
    sort_dic = sorted(dic.items(), key=lambda x: x[0])
    if sort_dic:
        print(sort_dic[0][0], sort_dic[0][1])
    else:
        print("No")
for k in [int(i) for i in input().split()]:
    isZishou(k)
    