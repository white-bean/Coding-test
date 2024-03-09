import sys
input = sys.stdin.readline
s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))
for _ in range(len(t)-len(s)):
    if t.pop() == 'A':
        continue
    else:
        t = t[::-1]
print(1 if s==t else 0)