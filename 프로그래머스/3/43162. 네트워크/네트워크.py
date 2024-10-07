from collections import deque

def bfs(i, n, computers, visited):
    q = deque([i])
    visited[i] = 1
    while q:
        a = q.popleft()
        for k in range(n):
            if k == a or visited[k]: continue
            if computers[a][k] == 1:
                q.append(k)
                visited[k] = 1
    return visited
            
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if not visited[i]:
            visited = bfs(i, n, computers, visited)
            answer += 1
    return answer