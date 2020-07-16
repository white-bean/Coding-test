# 2Xn을 2X1로 채우려고 하는데 타일 배치가 좌우 대칭이면 안됨
# 입력 : n
# 출력 : 경우의수

n = int(input())

cache = [-1 for i in range(n+1)]

def tile(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	if cache[n] != -1:
		return cache[n]

	cache[n] = tile(n-2) + tile(n-1)
	return cache[n]

result = tile(n)

if n==1:
	result=0
elif n==2:
	result=0
else:
	if n%2==1:
		result=result-tile(n//2)
	else:
		result=result-(tile(n//2)+tile(n//2-1))
		
print(result)
