from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    tmp = math.ceil((100-progresses[0])/speeds[0]); cnt = 0
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        if day > tmp:answer.append(cnt);tmp=day;cnt=1
        else:cnt+=1
    answer.append(cnt)
    
    return answer