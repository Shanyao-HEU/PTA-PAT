N, M = [int(i) for i in input().split()]
ques_dic = {}
for i in range(M):
    temp = [t for t in input().split()]
    ques_dic[i] = [temp[0], temp[1], temp[2], temp[2:]]

def func(stu, ques_dic):
    stu_dic = {}
    for i in range(len(stu)):
        temp = [t for t in stu[i][1:].split()]
        print("-------")
        print(temp)
        print("-------")
        stu_dic[i] = [temp[0], temp[1:]]
    score = 0
    wrong_lst = [0] * len(stu)
    for k in stu_dic.keys():
        if stu_dic[i][1] == ques_dic[i][3]:
            score += int(ques_dic[i][0])
        else:
            wrong_lst[i] = 1
    return score, wrong_lst

wrong_final = {i:0 for i in range(M)}    
for i in range(N):
    stu = [s for s in input().split(')')]
    print(stu)
    score, wrong_lst = func(stu, ques_dic)
    for c in range(M):
        wrong_final[c] += wrong_lst[c]
    print(score)
    
sort_wrong = sorted(wrong_final.items(), key=lambda x: (x[1], x[0]))
wrong_num = ''
for i, j in sort_wrong:
    wrong_num = wrong_num + str(i) + ' ' +str(j) + ' '
print(wrong_num[:-1])
    
    