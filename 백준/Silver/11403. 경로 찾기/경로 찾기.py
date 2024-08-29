import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for a in graph:
    print(" ".join(map(str, a)))