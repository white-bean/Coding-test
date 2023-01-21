from collections import deque

T = int(input())

def bfs(graph, i, j):
    qu = deque()
    qu.append((i, j))
    graph[i][j] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while qu:
        a, b = qu.popleft()
        for i in range(4):
            ny = a+dy[i]
            nx = b+dx[i]
            if ny<0 or ny>=N or nx<0 or nx>=M:continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                qu.append((ny, nx))

for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0

    graph = [[0]*M for _ in range(N)]
    for i in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt+=1
    print(cnt)
