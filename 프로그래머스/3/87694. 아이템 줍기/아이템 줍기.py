from collections import deque

def bfs(x, y, graph, itemX, itemY):
    q = deque([(0, x*2, y*2)])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while q:
        cnt, x, y = q.popleft()
        graph[y][x] = 1 # 방문 처리
        if (x == itemX*2) and (y == itemY*2):
            return cnt//2
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if graph[ny][nx] == 2:
                q.append((cnt+1, nx, ny))

def solution(rectangle, characterX, characterY, itemX, itemY):
    maxX, maxY = 0, 0
    for x1, y1, x2, y2 in rectangle:
        maxX = max(maxX, x2*2)
        maxY = max(maxY, y2*2)
    graph = [[0] * (maxX+2) for _ in range(maxY+2)]

    # 직사각형 내부 1로 채우기
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, x2*2+1):
            for y in range(y1*2, y2*2+1):
                graph[y][x] = 1
    # 직사각형 테두리 2로 바꾸기
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, x2*2+1):
            for y in range(y1*2, y2*2+1):
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if graph[y+j][x+i] == 0:
                            graph[y][x] = 2
                            break
    
    return bfs(characterX, characterY, graph, itemX, itemY)