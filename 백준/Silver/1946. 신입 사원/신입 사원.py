import sys
input = sys.stdin.readline
#1946 신입사원
T = int(input())
for _ in range(T):
    N = int(input())
    app = []
    for _ in range(N):
        dcm, itv = map(int, input().split())
        app.append([dcm, itv])
    app.sort(key=lambda x: (x[0], x[1]))
    #print(app)
    cnt = 1;min = app[0][1]
    for i in range(1, N):
        if min > app[i][1]:
            cnt+=1
            min=app[i][1]
    print(cnt)