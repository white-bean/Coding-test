def solution(money):
    house = len(money)
    buf = [money[0] for i in range(house)]
    buf2 = [0 for i in range(house)]
    
    # 첫번째 집 포함
    for i in range(2, house-1):
        buf[i] = max(buf[i-2]+money[i], buf[i-1])
    ans = buf[-2]
    
    # 마지막 집 포함
    buf2[1] = money[1]
    for i in range(2, house):
        buf2[i] = max(buf2[i-2]+money[i], buf2[i-1])
    ans2 = buf2[-1]
    
    return max(ans, ans2)