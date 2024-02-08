n = int(input())
for _ in range(n):
    li = []
    s = list(input())
    for st in s:
        if st == '(':
            li.append(st)
        elif st == ')':
            if li:
                li.pop()
            else:
                print('NO')
                break
    else:
        if not li:
            print("YES")
        else:
            print('NO')        