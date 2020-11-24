# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

def solution(m, n, puddles):
    cache = [[0]*(m+1) for i in range(n+1)]           # 각 위치의 거리값 저장할 배열 선언

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:                         # 집(시작위치)의 거리값 1로 설정
                cache[i][j] = 1
                continue
            if [j, i] in puddles:                     # 해당 위치에 물웅덩이 있을 경우 그 위치의 거리값 0으로 설정
                cache[i][j] = 0
                continue
            cache[i][j]=cache[i-1][j]+cache[i][j-1]   # 원소 a(i, j)의 거리값은 a(i-1, j) + a(i, j-1)
    return cache[n][m]%1000000007
