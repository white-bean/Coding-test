import sys
input = sys.stdin.readline

N = int(input())
T, P, dp = [0] * (N+2), [0] * (N+2), [0] * (N+2)
for i in range(1, N+1):
    a, b = map(int, input().split())
    T[i], P[i] = a, b

for i in range(1, N+1):
    if i+T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[N+1])