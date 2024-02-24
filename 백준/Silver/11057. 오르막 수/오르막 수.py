N = int(input())
DP = [[1]*10 for _ in range(N+1)]
if N == 1:
    print(sum(DP[1]))
else:
    for i in range(2, N+1):
        for j in range(10):
            DP[i][j] = sum(DP[i-1][j:10])
    print(sum(DP[N])%10007)