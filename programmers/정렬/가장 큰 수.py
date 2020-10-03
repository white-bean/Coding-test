# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

def solution(numbers):
    n=len(numbers)
    check=[0]*n
    if numbers == check:
        return "0"
    # 11번 테스트케이스의 경우가 [0, 0, 0, 0]인 경우이다. 이럴 경우 0만 출력되어야하므로 예외처리를 해주었다.
    
    numbers = list(map(str, numbers))   # 정수형 리스트를 문자형 리스트로 바꿔주고
    numbers = sorted(numbers, key = lambda x : (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]), reverse=True)  # 원소가 1000 이하이므로 4자리수를 비교해준다
    return ''.join(numbers)
    


# 다른 사람 풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)    
    return str(int(''.join(numbers)))

# [6, 10, 2]을 예시로 들면
# 문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교한다. 
# 물론 같으면, 다음 인덱스도 비교한다. 비교한 결과 [6, 2, 10]의 순으로 정렬된다.

# 마지막에 결과값 리턴시 정수형으로 바꾼 후 문자열로 한 번 더 바꾸는 이유는 ‘0’의 케이스를 대비하기 위해서이다. 
# [‘0’, ‘0’, ‘0’, ‘0’]이 주어졌을 때 join한 결과값이 ‘0000’이므로 이를 숫자 ‘0’으로 만들어주기 위해 두 번의 변경을 거찬다.

# str → int → str을 거치면 테스트케이스 11번을 통과할 수 있었다!! 기억하자
