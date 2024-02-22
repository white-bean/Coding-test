from collections import deque
import sys
input = sys.stdin.readline

N, L, R = list(map(int, input().split()))
pop = [list(map(int, input().split())) for _ in range(N)]

def bfs(graph, x, y, visited, flag):
    q = deque([(x, y)])
    visited[x][y] = flag
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt, ppl = 0, 0
    while q:
        a, b = q.popleft()
        cnt += 1
        ppl += graph[a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:continue
            if (visited[nx][ny]==0) & (L <= abs(graph[a][b]-graph[nx][ny]) <= R):
                visited[nx][ny] = flag
                q.append((nx, ny))
    return cnt, ppl

ans = 0
for _ in range(2000):
    visited = [[0]*N for _ in range(N)]
    pop2 = [[0]*N for _ in range(N)]
    flag = 1
    tmp = {}
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                tmp[flag] = bfs(pop, i, j, visited, flag)
                flag += 1
    if len(tmp)==N*N:
        print(ans)
        break

    for i in range(N):
        for j in range(N):
            pop2[i][j] = tmp[visited[i][j]][1]//tmp[visited[i][j]][0]
    
    ans += 1
    pop = pop2
