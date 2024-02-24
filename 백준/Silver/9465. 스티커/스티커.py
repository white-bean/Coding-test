import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    card = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0]*n for _ in range(2)]

    if n >= 1:
        DP[0][0] = card[0][0]
        DP[1][0] = card[1][0]
    if n >= 2:
        DP[0][1] = card[0][1] + card[1][0]
        DP[1][1] = card[1][1] + card[0][0]
    if n > 2:
        for i in range(2, n):
            DP[0][i] = max(DP[1][i-1] + card[0][i], DP[1][i-2] + card[0][i])
            DP[1][i] = max(DP[0][i-1] + card[1][i], DP[0][i-2] + card[1][i])

    print(max(DP[0][-1], DP[1][-1]))