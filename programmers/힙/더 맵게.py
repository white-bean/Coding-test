# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        if temp == 0: #예외일 때
            return -1
        if len(scoville) == 1 and scoville[0] < K: #예외일 때
            return -1
        heapq.heappush(scoville, temp)
        answer+=1
    return answer
    
# 예외상황을 잘 고려하자!


# 다른 사람 코드
import heapq

def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt

# try catch문을 이용해도 되었구나!
