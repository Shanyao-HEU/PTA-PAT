N = int(input())

result = ''

def wifi(inp):
    dic = {'A':'1', 'B':'2', 'C':'3', 'D':'4'}
    temp = [i[0] for i in inp.split(' ') if i[2]=='T']
    return dic[temp[0]]
    
for i in range(N):
    result += wifi(input())

print(result)