# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.


def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        num=0
        for j in range(i, len(prices)-1):
            if prices[i]>prices[j]:
                break
            else:
                num+=1
        answer.append(num)
    return answer
    
    
# 처음에 문제를 잘 이해를 못했어서... 예시로 보면 input이 [1, 2, 3, 2, 3]일 때 output이 [4, 3, 1, 1, 0]이다
# 1 -> 2, 3, 2, 3이므로 4
# 2 -> 3, 2, 3 이므로 3
# 3 -> 2로 떨어지므로 1
# 2 -> 3밖에 없으므로 1
# 3 -> 끝이므로 0

# 굳이 스택, 큐로 안 풀어도 되는....큼큼
