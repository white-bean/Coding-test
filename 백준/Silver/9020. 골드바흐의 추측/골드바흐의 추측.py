import sys
input = sys.stdin.readline
T = int(input())

def prime(n):
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True
    
for _ in range(T):
    n = int(input())
    a, b, d = 0, 0, 99999
    for i in range(2, n//2+1):
        if prime(i) and prime(n-i):
            if (n-2*i) < d:
                a, b, d = i, n-i, n-2*i
    print(a, b)
