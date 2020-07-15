#2X1, 1X2, 2X2 타일로 2Xn 짜리 직사각형 채우기

#입력 직사각형 가로 길이 n(1~100, 정수), 입력값 m(1~400, 정수)
#출력 경우의수를 m으로 나눈 나머지

n, m = map(int, input().split(" "))

#재귀
def tile(n):
	if n==1:
		return 1
	elif n==2:
		return 3
	else:
		return tile(n-1)+tile(n-2)*2
	
print(tile(n)%m)


#중복 제거
cache = [-1 for i in range(1001)]
def tile2(n):
	if n==1:
		return 1
	elif n==2:
		return 3
	
	if cache[n]!=-1:
		return cache[n]
	
	cache[n]=tile2(n-1)+tile2(n-2)*2
	return cache[n]

print(tile2(n)%m)
