import sys
from collections import deque
input = sys.stdin.readline

# 현재 아기상어 위치
# bfs로 물고기 크기가 1~아기상어크기 미만인 물고기 중 거리가 가장 짧은 물고기 찾기
# bfs 입력 : 현재 아기상어 위치, 출력 : 물고기 후보 리스트
# 그 위치로 아기상어 이동 : 시간 update
# queue, visitied 다 초기화

def bfs(graph, a, b, size): # 지도, 현재 아기상어 x, y 위치, 현재 아기상어 크기
    visited = [[0]*N for _ in range(N)]
    queue = deque([(0, a, b)]) # 시간, x좌표, y좌표
    eat_fish = []
    visited[a][b] = 1
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    while queue:
        time, a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx <0 or nx>=N or ny <0 or ny>=N: continue
            if visited[nx][ny]: continue

            if (graph[nx][ny] == size) or (graph[nx][ny] == 0): # 이동
                queue.append((time+1, nx, ny))
                visited[nx][ny] = 1

            elif graph[nx][ny] < size: # 냠냠
                queue.append((time+1, nx, ny))
                eat_fish.append((time+1, nx, ny))
                visited[nx][ny] = 1
    return sorted(eat_fish, key = lambda x: (x[0], x[1], x[2]))
    # 1순위 : 거리 가까운 물고기
    # 2순위 : 가장 위에 있는 물고기
    # 3순위 : 가장 왼쪽에 있는 물고기

N = int(input())
answer = 0
graph = []
a, b = 0, 0 # 아기상어 현재 위치
size = 2 # 아기상어 현재 크기
cnt = 0 # 아기상어 먹은 먹이 개수
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            a = i; b = j
            tmp[j] = 0 # 이 자리로도 이동가능해야하므로 0으로
    graph.append(tmp)

while True:
    eat_fish = deque(bfs(graph, a, b, size))
    if not eat_fish: break # 먹을 먹이가 없으면 엄마 콜!
    time, x, y = eat_fish.popleft()
    answer += time
    cnt += 1

    if size == cnt: # 자기 크기만큼 먹었으면 상어 크기 증가
        size += 1
        cnt = 0
    graph[x][y] = 0 # 그 위치 물고기 먹었으면 0으로 바꾸기
    a, b = x, y # 현재 상어 위치 update

print(answer)