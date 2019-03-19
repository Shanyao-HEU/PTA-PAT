a = input()
b = input()
res = ''
used = []
for i in a+b:
    if i not in used:
        used.append(i)
        res = res + i
    else:
        continue
print(res)