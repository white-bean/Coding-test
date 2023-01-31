import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
m = [list(input().strip()) for _ in range(N)]
for i in range(N):
    m[i] = list(map(int, m[i]))

def bfs(m, x, y):
    cnt = 1
    q = deque([(x, y)])
    m[x][y] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:continue
            if m[nx][ny] == 1:
                m[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

ap = 0
cnt = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            cnt.append(bfs(m, i, j))
            ap += 1
print(ap)
for i in sorted(cnt):
    print(i)