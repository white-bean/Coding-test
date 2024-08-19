import sys
input = sys.stdin.readline

N = int(input())
T, P, dp = [0] * (N+2), [0] * (N+2), [0] * (N+2)
result = 0 # 금액의 최대값
for i in range(1, N+1):
    a, b = map(int, input().split())
    T[i], P[i] = a, b

for i in range(1, N+2):
    dp[i] = max(dp[i], result)
    if i+T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    result = max(dp[i], result)
print(result)