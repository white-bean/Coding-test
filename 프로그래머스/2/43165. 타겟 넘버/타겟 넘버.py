from itertools import product

def solution(numbers, target):
    answer = 0
    for case in product([-1, 1], repeat = len(numbers)):
        tmp = 0
        for i, j in zip(numbers, case):
            tmp += (i*j)
        if target == tmp:
            answer += 1
    return answer