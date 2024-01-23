from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False]*(n+1)

def bfs(graph, start, visited):
    count=0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        count+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

print(bfs(graph, 1, visited)-1)




