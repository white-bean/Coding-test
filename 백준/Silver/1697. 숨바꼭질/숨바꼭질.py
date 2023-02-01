import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
q = deque()
visited = [False]*100001
q.append((0, N))
visited[N] = True
while q:
    cnt, n = q.popleft()
    if n == K:
        print(cnt)
        break
    if n-1>=0 and n-1<=100000 and not visited[n-1]: 
        q.append((cnt+1, n-1))
        visited[n-1] = True
    if n+1<=100000 and not visited[n+1]: 
        q.append((cnt+1, n+1))
        visited[n+1] = True
    if n*2<=100000 and not visited[2*n]: 
        q.append((cnt+1, 2*n))
        visited[2*n] = True
