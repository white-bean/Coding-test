from collections import deque

def bfs(graph, i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    dx = [0, 0, -1, -1, -1, 1, 1, 1]
    dy = [-1, 1, 0, -1, 1, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for k in range(8):
            nx = b + dx[k]
            ny = a + dy[k]
            if nx<0 or nx>=w or ny<0 or ny>=h:continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)