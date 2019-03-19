N, K = [int(i) for i in input().split()]
num_every = N // K

stu_hei = {}

for i in range(N):
    stu, hei = input().split()
    stu_hei[stu] = int(hei)

    
def sortRule1(x):
    stu = x[0]
    hei = x[1]
    return hei, -ord(stu[0]), -ord(stu[1]), -ord(stu[2])
    
sort_stu_hei = sorted(stu_hei.items(), key=sortRule1)

def sortRule2(stu_lst):
    sort_stu_lst = []
    i = 0
    stu_lst.reverse()
    while stu_lst:
        max_hei = stu_lst.pop(0)
        if i % 2 == 0:
            sort_stu_lst.append(max_hei)
            i += 1
        else:
            sort_stu_lst.insert(0, max_hei)
            i += 1
    sort_stu_lst = " ".join([stu[0] for stu in sort_stu_lst])
    return sort_stu_lst
    
for p in range(K-1, -1, -1):
    if p == K-1:
        stu_lst = sort_stu_hei[p*num_every:]
        print(sortRule2(stu_lst))
        
    else:
        stu_lst = sort_stu_hei[p*num_every:(p+1)*num_every]
        print(sortRule2(stu_lst))
    