n = int(input())
sch_scores = {}

for i in range(n):
    temp = [t for t in input().split()]
    if temp[2].lower() not in sch_scores:
        sch_scores[temp[2].lower()] = [(temp[0], temp[1])]
    else:
        sch_scores[temp[2].lower()].append([temp[0], temp[1]])

wei_scores = {}
for k, v in sch_scores.items():
    score = 0
    for stu in v:
        if stu[0][0] == 'T':
            score += int(stu[1])*1.5
        elif stu[0][0] == 'A':
            score += int(stu[1])
        elif stu[0][0] == 'B':
            score += int(stu[1])/1.5
    wei_scores[k] = [int(score), len(v)]

def sortRule(x):
    score = x[1][0]
    nums = x[1][1]
    name = x[0][0]
    name2 = x[0][1]
    return score, -nums, -ord(name), -ord(name2)
    

sort_wei_scores = sorted(wei_scores.items(), key=sortRule, reverse=True)
print(len(sort_wei_scores))

max = sort_wei_scores[0][1][0]
step = 1
print(sort_wei_scores)
for i, j in sort_wei_scores:
    if step == 1:
        print("{} {} {} {}".format(step, i, j[0], j[1]))
        step += 1
    else:
        if j[0] < max :
            max = j[0]
            print("{} {} {} {}".format(step, i, j[0], j[1]))
            step += 1
            
        else:
            print("{} {} {} {}".format(step-1, i, j[0], j[1]))
            step += 1

    