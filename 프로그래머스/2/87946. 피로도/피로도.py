from itertools import permutations

def check(k, case):
    result = 0
    for a, b in case:
        if k < a:
            break
        else:
            k -= b
            result += 1
    return result

def solution(k, dungeons):
    answer = -1
    for case in list(permutations(dungeons, len(dungeons))):
        answer = max(answer, check(k, case))
    return answer