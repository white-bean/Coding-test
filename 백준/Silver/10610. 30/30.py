from itertools import permutations
N = int(input())
tmp = sorted(list(map(int, str(N))), reverse=True)
#print(tmp)
if 0 not in tmp:
    print(-1)
else:
    if sum(tmp) % 3 == 0:
        print("".join(list(map(str, tmp))))
    else:
        print(-1)