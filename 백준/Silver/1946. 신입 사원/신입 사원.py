import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    app = []
    for _ in range(N):
        app.append(list(map(int, input().split())))
    app.sort(key=lambda x: x[0])
    cnt = 1;min = app[0][1]
    for i in range(1, N):
        if min > app[i][1]:
            cnt+=1
            min=app[i][1]
    print(cnt)