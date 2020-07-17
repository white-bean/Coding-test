# 조합 경우의 수 출력

def pick(n,picked,toPick):
    #기저사건
    if toPick==0:
        return picked

    if len(picked)==0:
        s=0
    else:
        s=picked[-1]+1

    for i in range(s,n,1):
        picked.append(i)
        pick(n,picked,toPcik-1)
        picked=picked[:-1]
