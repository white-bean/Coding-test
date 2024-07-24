# 완전탐색
def solution(s):
    answer = []
    n = len(s)
    if n == 1: return 1
    for i in range(1, n//2+1):
        tmp = ""
        cnt = 1
        tmp2 = s[:i]
        for j in range(i,n,i):
            if tmp2 == s[j:j+i]: cnt += 1
            else:
                tmp += str(cnt) + tmp2 if cnt >= 2 else tmp2
                cnt = 1
                tmp2 = s[j:j+i]
        tmp += str(cnt) + tmp2 if cnt >= 2 else tmp2
        answer.append(len(tmp))
    return min(answer)