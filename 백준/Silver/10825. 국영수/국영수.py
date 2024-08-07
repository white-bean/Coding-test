import sys
input = sys.stdin.readline
N = int(input())
alist = []
for _ in range(N):
    a, b, c, d = map(str, input().split())
    alist.append([a, int(b), int(c), int(d)])

alist.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for x in alist:
    print(x[0])