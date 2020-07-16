# 7X7 크기의 격자에 1부터 9까지 정수 쓰여있음
# 가장 왼쪽 위 칸에서 시작해 맨 오른쪽 아래 도착하는게 목표
# 각 칸에 쓰여진 숫자만큼 아래쪽 or 오른쪽으로 움직일 수 있음
# 격자 밖으로 벗어날 수 없다
# 입력 : 7X7 크기의 숫자들
# 출력 : 도달했을 시 1, 못 했을 시 0

board=[[int(i) for i in input().strip().split(' ')]for j in range(7)]

#cache = [[0]*7 for i in range(7)]


def jump(y, x):
	if y==6 and x==6:
		return True
	if y>6 or x>6:
		return False
	
	jumpsize = board[y][x]
	return jump(y+jumpsize, x) or jump(y, x+jumpsize)
	

print(int(jump(0, 0)))
	
	

	
