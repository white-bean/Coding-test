from collections import deque
import sys
input = sys.stdin.readline

N, L, R = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def bfs(visited, people, move, x, y, flag):
    q = deque([(x, y)])
    visited[x][y] = flag
    pos_list = [(x, y)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt, ppl = 1, people[x][y]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:continue
            if (visited[nx][ny] != flag) & (L <= abs(people[a][b]-people[nx][ny]) <= R):
                visited[nx][ny] = flag
                pos_list.append((nx, ny))
                cnt += 1
                ppl += people[nx][ny]
                q.append((nx, ny))
    if len(pos_list) > 1:
        move = True
        new_pop = ppl // cnt
        while pos_list:
            a, b = pos_list.pop()
            people[a][b] = new_pop

    return move, visited, people

flag = 1
for _ in range(2000):
    move = False
    for i in range(N):
        for j in range(N):
            if (visited[i][j] != flag):
                move, visited, people = bfs(visited, people, move, i, j, flag)

    if move:
        flag += 1
    else:
        print(flag-1)
        break