import sys
input = sys.stdin.readline
N = int(input())
alist = []
for _ in range(N):
    tmp = input().split()
    alist.append([tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])])

alist.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for x in alist:
    print(x[0])