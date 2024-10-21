# 각 지점 사이의 거리 최솟값이 x일 때, 제거해야 하는 바위 개수 비교하기
# [2, 11, 14, 17, 21]
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    start, end = 1, distance
    while start <= end:
        mid = (start+end)//2
        
        cnt, tmp = 0, 0
        for rock in rocks:
            if rock - tmp < mid:
                cnt += 1
            else:
                tmp = rock
        if cnt > n: 
            end = mid - 1
        else: 
            start = mid + 1
            answer = max(mid, answer)
    return answer