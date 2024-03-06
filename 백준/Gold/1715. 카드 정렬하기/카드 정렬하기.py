import heapq, sys
input = sys.stdin.readline
N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))
ans = 0
while len(card) > 1:
    a = heapq.heappop(card); b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    ans += (a+b)
print(ans)