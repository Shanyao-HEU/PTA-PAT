N, M = [int(i) for i in input().split()]

answer_list = []
error_list = [0 for i in range(M)]

for i in range(M):
    inp = input().split()
    score = int(inp[0])
    choice_num = int(inp[2])
    choice_lst = inp[3:]
    
    answer_list.append([score, choice_num, choice_lst])
    
score_list = [0 for i in range(N)]
    
for i in range(N):
    answers = input()
    answers = answers.replace("(", "")
    answers = answers.split(")")
    for j in range(M):
        answer = answers[j].strip().split()
        num = int(answer[0])
        correct = answer_list[j]
        ans = answer[1:]
        if ans == correct[2]:
            score_list[i] += correct[0]
        else:
            error_list[j] += i

for score in score_list:
    print(score)
max_error = max(error_list)
if max_error == 0:
    print("Too simple")
    
else:
    ret = []
    for ix, error_count in enumerate(error_list):
        if error_count == max_error:
            ret.append(str(ix))
    ret = [str(max_error)] + ret
    
    print(" ".join(ret))