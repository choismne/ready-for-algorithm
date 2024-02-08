from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    for i in range(n):
        li[i] = (li[i], i)

    queue = deque(li)

    count=0
    while queue:
        mx = max([i[0] for i in queue])
        res = queue.popleft()
        if res[0] >= mx:
            count+=1
            if res[1] == m:
                break
        else:
            queue.append(res)

    print(count)
