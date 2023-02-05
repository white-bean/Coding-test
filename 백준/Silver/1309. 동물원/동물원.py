import sys
input = sys.stdin.readline
N = int(input())
dp = [0]*(N+1)
dp2 = [0]*(N+1)
dp[0] = 1
dp[0] = 1
dp[1] = 3
dp2[1] = 1
for i in range(2, N+1):
    dp[i] = (dp[i-1] + 2*(dp[i-1] - dp2[i-1]))%9901
    dp2[i] = dp[i-1] - dp2[i-1]
print(dp[N])