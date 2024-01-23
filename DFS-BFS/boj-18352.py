from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start, visited, k):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    result = []

    while q:
        v, distance = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append((i, distance+1))
                visited[i] = True
                if distance+1 == k:
                    result.append(i)
    return result

result = bfs(graph, x, visited, k)
result.sort()

if len(result) == 0:
    print(-1)
else:
    for res in result:
        print(res)
                

        
        