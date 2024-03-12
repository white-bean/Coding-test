import sys
input = sys.stdin.readline
s1 = list(map(str, input().rstrip()))
s2 = list(map(str, input().rstrip()))
DP = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            DP[i+1][j+1] = DP[i][j] + 1

print(max(map(max, DP)))