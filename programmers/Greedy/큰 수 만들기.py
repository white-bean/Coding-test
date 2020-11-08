# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.


def solution(number, k):
    alist = list(number)    # 문자열을 리스트로
    answer = []
    answer.append(alist[0])
    for i in alist[1:]:
        while len(answer) > 0 and answer[-1] < i and k > 0:   # answer 원소 존재하고 최상위 스택이 i보다 작고 
                                                              # k(제거할 수 있는 횟수)가 남아있을 때 pop
            k-=1
            answer.pop()
        if len(answer) < len(number)-k:                       # answer의 길이는 number에서 k만큼 제거한만큼이므로
            answer.append(i)
    return (''.join(answer))                                  # 리스트에서 다시 문자열로
