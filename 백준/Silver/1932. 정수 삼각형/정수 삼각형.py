import sys
input = sys.stdin.readline
n = int(input())
tr = []
for _ in range(n):
    tr.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(i+1):
        tr[i][j] += max(tr[i+1][j], tr[i+1][j+1])

print(tr[0][0])
