from collections import deque

n, k = map(int, input().split())
per = []
queue = deque([i for i in range(1, n+1)])

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    per.append(queue.popleft())


print('<', end='')
print(', '.join(map(str, per)), end='')
print('>')

