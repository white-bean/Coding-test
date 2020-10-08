# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    num1 = [1, 2, 3, 4, 5]*2000                 # 1번 수포자가 찍는 방식
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250        # 2번 수포자가 찍는 방식
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000  # 3번 수포자가 찍는 방식

    cnt1, cnt2, cnt3 = [0, 1], [0, 2], [0, 3]   # 맞힌 개수와 인덱스 같이 있도록 하기 위해 리스트로 생성

    for i in range(len(answers)):               # 완전탐색
        if answers[i]==num1[i]:
            cnt1[0]+=1
        if answers[i]==num2[i]:
            cnt2[0]+=1
        if answers[i]==num3[i]:
            cnt3[0]+=1

    answer = []
    mlist = max(cnt1, cnt2, cnt3)
    if mlist[0]==cnt1[0]:                       # 1번 수포자부터 비교 후 넣기 때문에 출력되는 값은 오름차순
        answer.append(cnt1[1])
    if mlist[0]==cnt2[0]:
        answer.append(cnt2[1])
    if mlist[0]==cnt3[0]:
        answer.append(cnt3[1])
    
    return answer
    
    
# 다른 사람 풀이
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
    
# itertools에 cycle이라는 함수도 있다. 수포자들의 찍기 순서를 한개씩 출력해줄 수 있을 것 같다
# enumerate()을 써서 인덱스와 원소를 동시에 접근할 수도 있다!
# 수포자들의 찍기 순서를 나머지함수를 써서 비교해도 될 것 같다.
