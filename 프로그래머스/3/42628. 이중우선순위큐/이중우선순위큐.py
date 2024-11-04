import heapq
def solution(operations):
    answer = []
    for op in operations:
        a, b = op.split()
        if a == 'I':
            heapq.heappush(answer, int(b))
        elif not answer:
            pass
        elif b == '-1':
            heapq.heappop(answer)
        elif b == '1':
            answer.remove(max(answer))
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]