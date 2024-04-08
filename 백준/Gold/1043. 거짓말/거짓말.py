import sys
input = sys.stdin.readline

N, M = map(int, input().split())
true = set(input().split()[1:])
party = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for p in party:
        if p.intersection(true):
            true = true.union(p)

ans = 0
for p in party:
    if p.intersection(true):
        continue
    ans += 1

print(ans)