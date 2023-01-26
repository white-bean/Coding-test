from collections import deque
import sys
input = sys.stdin.readline #파이썬 입출력 속도 개선
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

dist = [-1]*(N+1)
dist[X] = 0
q = deque([X])
while q:
    a = q.popleft()
    for b in graph[a]:
        if dist[b] == -1:
            dist[b] = dist[a] + 1
            q.append(b)

flag = False
for i in range(N+1):
    if dist[i] == K:
        print(i)
        flag = True
if flag == False:
    print(-1)