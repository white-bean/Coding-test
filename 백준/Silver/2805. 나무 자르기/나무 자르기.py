import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

_min, _max = 1, max(trees)
while _min<=_max:
    mid = (_min+_max)//2
    res = 0
    for t in trees:
        if t > mid:
            res += t-mid
    if M <= res:
        _min = mid + 1
    else:
        _max = mid - 1
print(_max)