import sys, heapq
input = sys.stdin.readline

result = 0
hq = []
N = int(input())
for _ in range(N):
    heapq.heappush(hq, int(input()))

if N == 1: print(0)
else:
    while True:
        a, b = heapq.heappop(hq), heapq.heappop(hq)
        result += (a+b)
        if not hq: break
        heapq.heappush(hq, a+b)

    print(result)