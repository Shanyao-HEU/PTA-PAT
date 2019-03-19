def convBin(num):
    l = []
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return "".join(l[::-1])

    
def convSum(s):
    res = 0
    for i in s:
        if i.isalpha():
            i = i.lower()
            res = res + ord(i) - 96
    return res

 
s = input()
temp = list(convBin(convSum(s)))
print("{} {}".format(temp.count("0"), temp.count("1")))

