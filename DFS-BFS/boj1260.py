from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    #간선은 양방향이므로 양방향으로 인접리스트를 구성해주어야 한다. 
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

print(graph)

dfs_visited = [False]*(n+1)
bfs_visited = [False]*(n+1)


dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)