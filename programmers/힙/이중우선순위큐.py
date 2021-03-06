# operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
# operations의 원소는 큐가 수행할 연산을 나타냅니다.
# 원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.


def solution(operation): 
    answer = [] 
    temp = [] 
    for op in operation: 
        if op.split()[0] == 'I': 
            temp.append( int(op.split()[1]) ) 
        elif op.split()[0] == 'D': 
            if len(temp) != 0: 
                if op.split()[1] == '1': 
                    temp.remove(max(temp)) 
                elif op.split()[1] == '-1': 
                    temp.remove(min(temp)) 
    if len(temp) == 0: 
        answer = [0, 0] 
    else: answer = [max(temp), min(temp)] 
            
    return answer
