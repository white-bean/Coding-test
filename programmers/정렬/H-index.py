# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.


def solution(citations):
    citations = sorted(citations, reverse=True)   # 내림차순 정렬
    n = len(citations)
    answer=0
    for i in range(1, n+1):
        if i <= citations[i-1]:     # 해당 인덱스(i=1, 2, 3, ...)와 정렬된 원소값 비교 후 만약 인덱스가 크면 stop
            answer+=1
        else:
            break
    return answer
    
  
  
  
# 문제 이해하는게 더 어려운....
