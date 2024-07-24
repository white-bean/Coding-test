import sys
input = sys.stdin.readline
N, M = map(int, input().split())
chicken = []; home = []

for i in range(N): # 각 주소 좌표 저장
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1: home.append((i, j))
        elif tmp[j] == 2: chicken.append((i, j)) 

visited = [False]*len(chicken)
result = 9999999

def dfs(cnt, idx):
    global result
    if cnt == M:
        dist = 0
        for x, y in home:
            tmp = 9999999
            for i in range(len(chicken)):
                if visited[i]:
                    tmp = min(tmp, abs(chicken[i][0] - x) + abs(chicken[i][1] - y))
            dist += tmp 
        result = min(result, dist)
    for i in range(idx, len(chicken)):
        visited[i] = True
        dfs(cnt+1, i+1)
        visited[i] = False

dfs(0, 0)
print(result)