def solution(citations):
    result = 0
    citations.sort(reverse=True)
    #print(citations)
    for i, k in enumerate(citations):
        if k >= (i+1): result = i+1
    return result