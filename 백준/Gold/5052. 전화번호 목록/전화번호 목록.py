import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cases = sorted([input().rstrip() for _ in range(n)])
    ans = 'YES'
    for i in range(n-1):
        if cases[i+1].startswith(cases[i]):ans='NO';break
    print(ans)