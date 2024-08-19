def calculating(X, Y):
    result = set()
    for x in X:
        for y in Y:
            result.add(x+y)
            result.add(x-y)
            result.add(y-x)
            result.add(x*y)
            if y != 0:
                result.add(x//y)
    return result

def solution(N, number):
    answer = -1
    if N == number: return 1
    dp = {}
    dp[1] = {N}
    for i in range(2, 9):
        temp = {int(str(N)*i)}
        for j in range(1, i):
            temp.update(calculating(dp[j], dp[i-j]))
        if number in temp:
            answer = i
            break
        dp[i] = temp
    return answer