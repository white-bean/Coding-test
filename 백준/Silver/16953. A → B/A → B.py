from collections import deque
A, B = map(int, input().split())

q = deque()
q.append((A, 1))
ans = -1
while q:
    n, cnt = q.popleft()
    if n == B:ans = cnt
    if n*2 <= B: q.append((n*2, cnt+1))
    if int(str(n)+'1') <= B: q.append((int(str(n)+'1'), cnt+1))
print(ans)
