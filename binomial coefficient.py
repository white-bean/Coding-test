#입력: 최대 100의 양의 정수
n, k = map(int, input().split(" "))

#재귀
def binomial(n, k):
	if k==1:
		return n
	if n==k:
		return 1
	else:
		return binomial(n-1, k-1)+binomial(n-1, k)

#중복 제거
cache=[[-1 for i in range(101)] for j in range(101)]

def bino(n, r):
	if n==r:
		return 1
	if r==1:
		return n
	if cache[n][r] != -1:
		return cache[n][r]
	
	cache[n][r]=bino(n-1, r-1)+bino(n-1, r)
	return cache[n][r]


print(binomial(n, k))
print(bino(n, k))
