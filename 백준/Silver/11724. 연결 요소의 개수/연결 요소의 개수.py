from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

result = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        result += 1

print(result)