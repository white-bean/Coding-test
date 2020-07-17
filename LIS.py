# 최대 증가 부분 수열
# 입력: 원소개수, 수열
# 출력: 최대 증가 부분 수열의 길이

n=int(input())
s=list(map(int,input().strip().split(" ")))

cache=[-1 for i in range(100)]

def lis(start):
	tmp=cache[start+1]
	if tmp!=-1:
		return tmp
	tmp=1
	for i in range(start+1,n,1):
		if start ==-1 or s[start]<s[i]:
			tmp = max(tmp,lis(i)+1)
	return tmp

print(lis(0))
