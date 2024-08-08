def solution(N, stages):
    answer = []
    cnt = len(stages)
    for i in range(1, N+1):
        c = stages.count(i)
        tmp = c/cnt if cnt != 0 else 0
        answer.append((i, tmp))
        cnt -= c
    answer.sort(key=lambda x: (-x[1], x[0]))
    return list(x[0] for x in answer)