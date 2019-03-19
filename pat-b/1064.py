input()
nums = [i for i in input().split()]
fri = []
for num in nums:
    temp = 0
    for n in num:
        temp += int(n)

    if temp not in fri:
        fri.append(temp)
       
fri.sort()     
fri = [str(f) for f in fri]
print(len(fri))
print(" ".join(fri))
        
