import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    try:
        if x == 0:
            print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)
    except:
        print(0)