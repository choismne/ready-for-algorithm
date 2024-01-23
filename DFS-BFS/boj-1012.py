#유기농 배추
#리스트로 주어지고 상하좌우가 연결된 그래프 형태 문제

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y, n, m):
    if graph[x][y] == 0:
        return False
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= n or ny < 0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
    return True

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if bfs(graph, i, j, n, m):
                cnt += 1
    print(cnt)