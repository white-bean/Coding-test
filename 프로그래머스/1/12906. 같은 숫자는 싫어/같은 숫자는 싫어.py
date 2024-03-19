def solution(arr):
    answer = []
    tmp = 0
    for i in arr:
        if (i not in answer) or (i != tmp):answer.append(i);tmp=i
        else:continue
    return answer