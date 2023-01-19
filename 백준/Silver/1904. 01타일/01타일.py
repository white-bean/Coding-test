# 재귀로 풀면 메모리 초과
N = int(input())
dp=[i for i in range(N+2)]
for i in range(3, N+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746
print(dp[N])