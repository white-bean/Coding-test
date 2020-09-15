# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

# solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge=[0]*bridge_length

    while bridge:   # 리스트 비어있으면 stop
        time+=1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time
    
   
   
# truck_weights = truck_weights[::-1] 초반에 이렇게 뒤집어 주면 pop(0) 대신 pop()을 쓸 수 있어 더 효율적이다.

# bridge를 bridge_length만큼 만들고 넣었다 뺐다하면 되는 문제.....후
