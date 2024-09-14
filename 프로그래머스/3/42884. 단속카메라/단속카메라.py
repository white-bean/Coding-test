def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x: x[1])
    current_camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > current_camera:
            answer += 1
            current_camera = routes[i][1]
    return answer