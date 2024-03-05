N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
ans = 0
if A == B:print(0)
elif (N < 3) or (M < 3):print(-1)
else:
    for i in range(0, N-2):
        for j in range(0, M-2):
            if A[i][j] == B[i][j]: continue
            else:
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        A[a][b] = 1-A[a][b]
                ans+=1
                if A==B:print(ans);exit(0)
    print(-1)