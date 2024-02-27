n = int(input())
check = False

for i in range(n):
    sum=i
    li = list(str(i))
    for l in li:
        sum += int(l)
    if sum == n:
        print(i)
        check = True
        break

if not check:
    print(0)

        
