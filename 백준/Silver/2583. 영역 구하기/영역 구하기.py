import sys
from collections import deque
input = sys.stdin.readline
M, N, K = map(int, input().split())
area = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            area[i*(-1)+(M-1)][j] = 1

def bfs(area, a, b):
    q = deque()
    q.append((a, b))
    area[a][b] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = b + dx[k]
            ny = a + dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=M:continue
            if area[ny][nx] == 0:
                area[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt
cnt = 0
V = []
for i in range(M):
    for j in range(N):
        if area[i][j] == 0:
            V.append(bfs(area, i, j))
            cnt += 1
print(cnt)
print(*sorted(V))