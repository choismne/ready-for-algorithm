# #예시에서는 dfs로 풀지만 bfs로도 풀어보자. 
# from collections import deque

# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(graph, x, y):
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] == 1

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
