H, U, D, F = map(int, input().split(" "))

current=0
day=0
slide=U*(F/100)
result=True

while result:
	day+=1
	current+=U
	if(current>H):
		break
	current-=D
	U-=slide
	if(current<0):
		result=False

if result:
	print("Success %d" %day)
else:
	print("Failure")
