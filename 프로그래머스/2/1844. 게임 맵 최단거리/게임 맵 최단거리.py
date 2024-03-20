from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(1, 0, 0)])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while queue:
        cnt, a, b = queue.popleft()
        if (a, b) == (n-1, m-1): return cnt
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
            if maps[nx][ny] == 1:
                queue.append((cnt+1, nx, ny))
                maps[nx][ny] = 0
    return -1

def solution(maps):
    return bfs(maps)