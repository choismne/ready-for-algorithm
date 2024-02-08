n = int(input())
stack = []
result=[]
flag = True

inp = 1
for _ in range(n):
    want = int(input())
    while inp <= want:
        stack.append(inp)
        inp+=1
        result.append('+')
    if stack[-1] == want:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if not flag:
    print('NO')
else:
    for rs in result:
        print(rs)