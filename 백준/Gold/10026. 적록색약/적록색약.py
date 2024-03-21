from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
area = [list(input().split()[0]) for _ in range(N)]
area2 = [list(map(lambda x:x.replace('G', 'R'), alist)) for alist in area]

def bfs(graph, x, y, visited):
    q = deque([(x, y)])
    RGB = graph[x][y]
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <0 or nx >=N or ny<0 or ny>=N:continue
            if (graph[nx][ny] == RGB) & (visited[nx][ny]==0):
                visited[nx][ny] = 1
                q.append((nx, ny))

cnt, cnt2 = 0, 0
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(area, i, j, visited)
            cnt+=1
        if visited2[i][j] == 0:
            bfs(area2, i, j, visited2)
            cnt2+=1

print(cnt, cnt2)
