N = list(input())
if '0' not in N:
    print(-1)
else:
    if sum(map(int, N)) % 3 == 0:
        print("".join(sorted(N, reverse=True)))
    else:
        print(-1)