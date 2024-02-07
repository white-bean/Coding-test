N = input()
tmp = sorted(N, reverse=True)
if '0' not in tmp:
    print(-1)
else:
    if sum(list(map(int, tmp))) % 3 == 0:
        print("".join(tmp))
    else:
        print(-1)