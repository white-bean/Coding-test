import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF: print('INF')
    else: print(distance[i])