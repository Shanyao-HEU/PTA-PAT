n, m = map(int, input().split())
scores = {}
for i in range(n):
    stu, score = input().split()
    scores[stu] = int(score)
    
for i in range(m):
    cate, kind = input().split()
    if cate == '1':
        temp = [(k, scores[k]) for k in scores if k[0] == kind]
        sort_temp = sorted(temp, key=lambda x: (x[1], -ordx[0]))
        print("Case {}: {} {}".format(i, cate, kind))
        
    elif cate == '2':
        temp = [(k, scores[k]) for k in scores if k[1:4] == kind]
        print("Case {}: {} {}".format(i, cate, kind))
        print(len(temp), sum([scores[k] for k in temp]))
    
    else:
        temp = [(k, scores[k]) for k in scores if k[4:10] == kind]
        if temp:
            dates = []
            for k2, v2 in temp:
                if temp
        else:
            print("NA")