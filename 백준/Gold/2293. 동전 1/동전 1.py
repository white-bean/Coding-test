import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    tmp = int(input())
    if tmp > k:continue
    else:coin.append(tmp)
coin.sort()

DP = [0]*(k+1)
DP[0] = 1
for c in coin:
    for i in range(c, k+1):
        DP[i] += DP[i-c]

print(DP[k])