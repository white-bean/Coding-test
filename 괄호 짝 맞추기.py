# 입력 : 임의의 괄호 배치
# 출력 : 짝이 맞으면 True, 아니면 False

alist = input()

def pair(alist):
	opening=["[", "{", "("]
	closing=["]", "}", ")"]
	stack=[]
	
	for s in alist:
		if s in opening:
			stack.append(s)

		else:
			if len(stack)==0:
				return False
			if closing[opening.index(stack[-1])] != s:  #stack의 최상단이 짝이 맞을 때
				return False
			stack.pop()

	if not stack: #stack 비어있을 때
		return True
	else: #stack 원소 남아있을 때
		return False
	
	
print(pair(alist))

	
