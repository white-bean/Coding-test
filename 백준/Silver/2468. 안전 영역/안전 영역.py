from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, i, j, h, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <0 or nx>=N or ny <0 or ny>=N: continue
            if (graph[nx][ny] > h) & (visited[nx][ny]==0):
                visited[nx][ny] = 1
                q.append((nx, ny))

result = []
for h in range(max(map(max, area))):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (area[i][j] > h) & (visited[i][j]==0):
                bfs(area, i, j, h, visited)
                cnt += 1
    result.append(cnt)

print(max(result))
