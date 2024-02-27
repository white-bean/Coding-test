import sys
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [0]*(K+1)
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w-1, -1):
        DP[i] = max(DP[i], DP[i-w]+v)

print(DP[-1])