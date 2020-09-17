# 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
# 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
# location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.


def solution(priorities, location):
    index = [i for i in range(0, len(priorities))]  # priorities 배열 인덱스를 담아두는 리스트

    i=0
    while 1:
        if priorities[i] < max(priorities[i+1:]):
            priorities.append(priorities.pop(i))
            index.append(index.pop(i))
        else:
            i+=1
        if priorities == sorted(priorities, reverse=True):
            break
        
    return index.index(location)+1
    
    
# 다른 사람 코드
def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])   # enumerate : 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
