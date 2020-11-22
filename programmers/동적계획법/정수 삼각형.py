# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

def solution(triangle):
    answer = 0
    k=len(triangle)
    best=[[0]*(len(triangle[k-1])+1) for i in range(k+1)]     # best(r, c) : 레벨 1에 있는 원소부터 시작해 레벨 r의 c번째 원소에서 끝나는 최적 경로의 값
                                                              # 1<=r<=k, 1<=c<=r, k=레벨
    for i in range(1, k+1):
        for j in range(1, i+1):
            best[i][j] = triangle[i-1][j-1]+max(best[i-1][j-1], best[i-1][j])   # 원소 a(r, c)까지 오는 경로는 원소 a(r-1, c-1)과 a(r-1, c) 중 큰 값을 갖는 경로 택하면 됨
        
    for i in range(1, k+1):
        if answer < best[k][i]:
            answer = best[k][i]     # best 배열의 가장 마지막 원소에서 최댓값을 찾으면 그 값이 원하는 최적의 값

    return answer
    
# 동적계획법의 완전 기본 문제인 숫자 삼각형 문제였다!!! 알고리즘 전공 수업시간에도 배운 것이므로 꼭꼭 이해&암기하자
