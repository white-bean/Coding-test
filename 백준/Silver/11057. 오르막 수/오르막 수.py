N = int(input())
DP = [1]*10
for i in range(1, N):
    for j in range(1, 10):
        DP[j] += DP[j-1]
print(sum(DP)%10007)