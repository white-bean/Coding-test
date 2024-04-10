def solution(number, k):
    number = list(number)
    answer = [number[0]]
    for s in number[1:]:
        while len(answer) > 0 and answer[-1] < s and k > 0:
            answer.pop()
            k -= 1
        if len(answer) < len(number) - k:
            answer.append(s)
    return ''.join(answer)