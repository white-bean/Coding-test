# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# 구명보트는 작아서 한 번에 최대 2명씩.... 이걸 안 읽어서 처음에 삽질함 → 문제를 꼼꼼히 읽자!


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)           # 내림차순 정렬
    
    for num in people:
        answer+=1
        if limit - num >= people[-1]:   # 가장 큰 무게와 가장 작은 무게가 탈 수 있을 때
            people.pop()                # 가장 큰 무게 인덱스는 어차피 for문으로 돌아가므로 가장 작은 무게일 때만 제거
                        
    return answer
