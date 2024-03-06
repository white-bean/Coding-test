import heapq

N = int(input())
card = []; ans = 0
for _ in range(N):
    heapq.heappush(card, int(input()))
ans = 0
if len(card) == 1:print(0);exit(0)
while card:
    a = heapq.heappop(card); b = heapq.heappop(card)
    if card:heapq.heappush(card, a+b)
    ans += (a+b)
print(ans)