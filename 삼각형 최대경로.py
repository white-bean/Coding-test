#입력: 삼각형 높이, 삼각형 이루는 각 정수
#출력: 맨 위에서 시작해 아래로 올 때까지 최대 경로

n=int(input())
tri=[[int(i) for i in input().strip().split(" ")] for j in range(n)]
cache=[[-1 for i in range(n)] for j in range(n)]
def path(y,x):
	if y==n-1:
		return tri[y][x]
	tmp=cache[y][x]
	if tmp!=-1 :
		return tmp
	return max(path(y+1,x),path(y+1,x+1))+tri[y][x]

print(path(0,0))
