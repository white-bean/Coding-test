#계단 최대 2칸 오를 수 있다!
#입력 num(30이하 정수)
#출력 계단 오르는 경우의 수

num = int(input())

#재귀
def stairs(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	return stairs(n-1)+stairs(n-2)
	
print(stairs(num))


#중복제거버전
cache = [-1 for i in range(31)]

def stairs2(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	
	if cache[n] != -1:
		return cache[n]
	
	cache[n] = stairs2(n-1)+stairs2(n-2)
	return cache[n]

print(stairs2(num))
	
