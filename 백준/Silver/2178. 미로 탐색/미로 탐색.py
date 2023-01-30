import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
road = [list(input().strip()) for _ in range(N)]
for i in range(N):
    road[i] = list(map(int, road[i]))

def bfs(road, N, M):
    q = deque([(1, 0, 0)])
    road[0][0] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        cnt, a, b = q.popleft()
        if (a,b) == (N-1, M-1): return cnt
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:continue
            if road[nx][ny] == 1:
                road[nx][ny] = 0
                q.append((cnt+1, nx, ny))

print(bfs(road, N, M))