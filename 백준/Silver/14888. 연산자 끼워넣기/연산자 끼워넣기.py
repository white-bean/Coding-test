import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) # +, -, x, //
operators = ['+']*cal[0]+['-']*cal[1]+['*']*cal[2]+['//']*cal[3]
result = []
for alist in list(permutations(operators, N-1)):
    res = num[0]
    for i in range(1, N):
        if alist[i-1] == '+':
            res += num[i]
        elif alist[i-1] == '-':
            res -= num[i]
        elif alist[i-1] == '//':
            if res < 0:
                res = (res*(-1) // num[i])*(-1)
            else: res //= num[i]
        else:
            res *= num[i]
    result.append(res)
print(max(result))
print(min(result))