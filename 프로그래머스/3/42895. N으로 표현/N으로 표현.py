def solution(N, number):
    answer = 0
    if N==number: return 1
    DP = [{int(str(N)*i)} for i in range(1, 9)]
    for i in range(1, 8):
        for j in range(i//2+1):
            for num in list(DP[j]):
                for num2 in list(DP[i-j-1]):
                    DP[i].add(num+num2)
                    DP[i].add(num-num2)
                    DP[i].add(num2-num)
                    DP[i].add(num*num2) 
                    if num != 0: DP[i].add(num2//num)
                    if num2 != 0: DP[i].add(num//num2)
        if number in list(DP[i]):
            return i+1
    return -1