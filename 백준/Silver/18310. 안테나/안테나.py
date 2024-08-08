import sys
input = sys.stdin.readline

N = int(input())
locations = sorted(list(map(int, input().split())))
print(locations[(N-1)//2])