# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 
# 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    queue2 = deque(speeds)
    
    days=0
    answer = []
    cnt=0
    while len(queue)>0:
        if days*queue2[0]+queue[0]>=100:  # 작업량 100%를 채우면
            queue.popleft()
            queue2.popleft()
            cnt+=1
        else:
            days+=1
            if cnt>0:
                answer.append(cnt)
                cnt=0
    answer.append(cnt)
    return answer
    
    
# 다른 사람 코드
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):  //progresses와 speeds 순차적 접근
        if len(Q)==0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s),1])   //[days, cnt]
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

