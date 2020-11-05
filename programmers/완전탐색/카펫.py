# 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

import math
def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow))+1):  # yellow의 루트값만큼으로 제한
        if yellow%i==0:                           # i가 yellow의 약수일 때 (나눠질 때)
            hori = yellow/i                       # yellow의 가로 길이
            t_b = 2*(hori+i)+4                    # 특정 yellow일 때 이를 둘러싸는 brown의 개수
            if t_b == brown:                      # 특정 brown의 개수가 주어진 brown의 개수랑 동일할 때
                return [hori+2, i+2]              # 카펫의 가로세로값 리턴
    return False
