# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    def dfs(L, total):                  # L:레벨, total:덧셈or뺄셈한 값
        if L == n:                      # 주어진 갯수와 트리의 레벨이 같을 때
            if total == target:         # 계산한 값과 주어진 target 값이 같다면
                nonlocal cnt            # 함수 밖에 있는 지역변수 접근하기 위해 nonlocal 사용
                cnt += 1                # cnt++
        else:                           # 레벨과 갯수가 맞지 않다면 덧셈과 뺄셈을 진행하며 트리 확장
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
    
    dfs(0,0)
    return cnt
