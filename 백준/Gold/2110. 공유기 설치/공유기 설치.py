# 특정 거리일 때 설치할 수 있는 공유기 개수를 따져보자

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted(list(int(input()) for _ in range(N)))

if C == 2: print(home[-1] - home[0])
else:
    start, end = 1, home[-1] - home[0]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt, tmp = 1, home[0]
        for i in range(1, N):
            if home[i] >= tmp + mid:
                cnt += 1
                tmp = home[i]
        if cnt >= C:
            start = mid + 1
            result = mid if mid > result else result
        else:
            end = mid -1
    print(result)
