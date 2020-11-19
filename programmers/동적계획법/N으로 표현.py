# 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

def solution(N, number):
    answer = -1
    if N==number:
        return 1
    buf = [{int(str(N)*i)} for i in range(1, 9)]  # N 1개 사용, 2개 사용, 3개 사용, ..., 8개 사용(8 초과일 경우 -1 리턴이므로), 중복제거위해 set 사용(처음에 안했다가 시간초과남...)
    for i in range(1, len(buf)):
        for j in range(i):
            for num1 in buf[j]:
                for num2 in buf[i-j-1]:
                    buf[i].add(num1+num2)
                    buf[i].add(num1-num2)
                    buf[i].add(num2-num1)
                    buf[i].add(num1*num2)
                    if num2!=0:
                        buf[i].add(num1//num2)
                    if num1!=0:
                        buf[i].add(num2//num1)
        if number in buf[i]:
            answer=i+1
            break
    return answer
    

# 효율성 높이기 위해 2번째 for문 for j in range(i//2+1): 으로 개선가능!!
# N=2인 경우 N=1, N=1 고려, N=3인 경우 N=2, N=1 고려
# 앞의 경우가 중복되기 때문에 절반만 확인해도 됨!
