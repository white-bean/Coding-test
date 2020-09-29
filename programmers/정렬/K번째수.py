# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.

# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(array, commands):
    answer = []
    for alist in commands:      # for i, j, k in commands: 라고 간단하게 써도 될 듯 하다!
        i = alist[0]
        j = alist[1]
        k = alist[2]
        answer.append(sorted(array[i-1:j])[k-1])  # i-1부터 j-1까지 자르고 정렬한 뒤 (k-1)로 접근한 값
    return answer

# a=[]가 있을 때 
# a.sort()는 리스트 자체를 정렬하는 것이고
# sorted(a)는 정렬된 새로운 리스트를 리턴한다.



# 축약버전
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
