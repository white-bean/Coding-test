def solution(brown, yellow):
    answer = []
    for i in range(1, brown//4 + 1):
        a = i
        b = (brown - 2*i)//2 - 2
        if a*b == yellow:
            answer.append(b+2)
            answer.append(a+2)
            break
    return answer