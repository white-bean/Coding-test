from collections import deque
import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    I = int(input())
    a, b = map(int, input().split(" "))
    A, B = map(int, input().split(" "))

    graph = [[0]*I for _ in range(I)]

    def bfs(graph, I):
        queue = deque([(0, a, b)])
        graph[a][b] = -1
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [-1, -2, -2, -1, 1, 2, 2, 1]
        while queue:
            cnt, n, m = queue.popleft()
            if (n, m) == (A, B): return cnt
            for i in range(8):
                nx = n+dx[i]
                ny = m+dy[i]
                if nx <0 or nx>=I or ny<0 or ny>=I:continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = -1
                    queue.append((cnt+1, nx, ny))

    print(bfs(graph, I))