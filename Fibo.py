#피보나치 수의 n번째 항까지의 합 출력하기

def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibo(n-2)+fibo(n-1)
	
num=int(input())

result=0
for i in range(1, num+1):
	result+=fibo(i)

print(result)
