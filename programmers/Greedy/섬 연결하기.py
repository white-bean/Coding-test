# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 
# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

# Kruskal의 알고리즘 이용하기!!! - 사이클없이 각 단계에서 그래프의 모든 에지 중 최소의 가중치 갖는 에지 선택하는 방법

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])   # 비용기준 오름차순으로 정렬
    check = set([costs[0][0]])        # 정점이 같은 성분에 있는지 체크하기 위해 중복 제거해주는 set 사용
    
    while len(check)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in check and cost[1] in check:   # 같은 성분에 있을 때
                continue
            elif cost[0] in check or cost[1] in check:  # 두 정점이 같은 성분에 있지 않을 때
                check.update([cost[0], cost[1]])
                answer+=cost[2]                         # +비용
                costs.pop(i)
                break

    return answer
