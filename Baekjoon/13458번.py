import sys
N = int(sys.stdin.readline())
answer = N
ppl = list(map(int, sys.stdin.readline().split()))
A, B = map(int, sys.stdin.readline().split())
for num in ppl:
    num -= A
    if num > 0:
        if num%B==0:
            answer += num//B
        else:
            answer += num//B + 1
print(answer)
