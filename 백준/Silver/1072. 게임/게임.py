import sys, math
input = sys.stdin.readline

X, Y = map(int, input().split())
start, end = 1, 10**9
Z = math.trunc((Y*100)/X)
while start <= end:
    mid = (start + end) // 2
    new_Z = math.trunc(((Y+mid)*100)/(X+mid))
    if new_Z > Z: 
        end = mid - 1
    else: start = mid + 1

print(start if start <= 10**9 else -1)