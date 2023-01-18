from collections import Counter

N = int(input())
num = [int(input()) for _ in range(N)]

avg = sum(num)/N
if avg > 0:
    print(int(avg) + (1 if abs(avg-int(avg))>=0.5 else 0))
else:
    print(int(avg) + (-1 if abs(avg-int(avg))>=0.5 else 0))

print(sorted(num)[N//2])

mod = sorted(Counter(num).most_common(), key=lambda x: (-x[1], x[0]))
if len(num) > 1:
    print(mod[0][0] if mod[0][1] > mod[1][1] else mod[1][0])
else:
    print(num[0])

print(max(num) - min(num))