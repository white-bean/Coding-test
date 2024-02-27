import sys
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        DP[i][j] = DP[i-1][j] if w > j else max(v+DP[i-1][j-w], DP[i-1][j])

print(DP[-1][-1])