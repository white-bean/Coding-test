# 여러 줄 입력받는데 마지막에 엔터 없을 때 -> EOF error

age = int(input())
heart = 220-age
a=0
b=0
c=0
d=0
e=0
f=0
while True:
	try:
		num = int(input())
		if num/heart*100 >= 90:
			a+=1
		elif num/heart*100 >= 80:
			b+=1
		elif num/heart*100 >= 75:
			c+=1
		elif num/heart*100 >= 68:
			d+=1
		elif num/heart*100 >= 60:
			e+=1
		else:
			f+=1
	except EOFError:
		break


print(a, b, c, d, e, f)
