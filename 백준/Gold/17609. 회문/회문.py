import sys
input = sys.stdin.readline

def simple_check(s):
    for i in range(len(s)//2):
        tmp = s.pop()
        if s[i] != tmp: s.append(tmp); return i
    return -1

def check(s):
    i = simple_check(s)
    if i == -1:return 0
    else:
        s2 = s.copy()
        if simple_check(s[i+1:])==-1:return 1
        elif simple_check(s2[i:-1])==-1:return 1
        else:return 2

T = int(input())
for _ in range(T):
    s = list(map(str, input().rstrip()))
    print(check(s))