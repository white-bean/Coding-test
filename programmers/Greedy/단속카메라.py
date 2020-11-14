# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 
# 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

def solution(routes):
    answer = 0
    routes.sort()         # 진입한 지점 기준으로 오름차순 정렬
    end = routes[0][1]    # 이전 차량의 도착점
    answer+=1             # 일단 카메라 1대 설치
    
    for s, e in routes[1:]:
        if s > end:       # 현재 차량의 시작지점이 이전 차량의 도착점보다 클 때
            answer+=1     # 포함관계 벗어나므로 카메라 설치
            end = e       # 도착점을 현재 차량의 도착지점으로

        else:             # 포함관계일 때
            end = min(e, end) # 이전 도착지점과 현재 도착지점 중 작은걸로
        
    return answer
