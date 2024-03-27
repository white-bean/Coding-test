import sys
input = sys.stdin.readline

def check(rec1, rec2):
    if ((rec1[2], rec1[1])==(rec2[0], rec2[3])) or ((rec1[2], rec1[3])==(rec2[0], rec2[1])):
        return 'c'
    elif (rec1[2] < rec2[0]) or (rec1[3] < rec2[1]) or (rec2[3] < rec1[1]):
        return 'd'
    elif (rec1[1]==rec2[3]) or (rec1[2]==rec2[0]) or (rec1[3]==rec2[1]):
        return 'b'
    else:
        return 'a'
    
for _ in range(4):
    R = list(map(int, input().split()))
    if R[0] <= R[4]:
        rec1, rec2 = R[:4], R[4:]
    else:
        rec1, rec2 = R[4:], R[:4]

    print(check(rec1, rec2))

