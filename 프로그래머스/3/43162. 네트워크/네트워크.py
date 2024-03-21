from collections import deque

def bfs(node, graph, visited, n):
    queue = deque([node])
    visited[node] = 1
    while queue:
        node = queue.popleft()
        for i in range(n):
            if i != (node-1) and graph[node-1][i] and not visited[i+1]:
                queue.append((i+1))
                visited[i+1] = 1

def solution(n, computers):
    answer = 0
    visited = [0]*(n+1)
    for node in range(1, n+1):
        if not visited[node]:
            bfs(node, computers, visited, n)
            answer += 1
    return answer