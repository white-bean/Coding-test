# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.

# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요


def solution(clothes):
    dict = {}
    for type in clothes:            # 딕셔너리에 종류 : 개수로 저장
        if type[1] in dict.keys():  
            dict[type[1]]+=1
        else:
            dict[type[1]]=1
            
    cnt=1
    for num in dict.values():
        cnt*=(num+1)                # 안 입는 경우까지 1을 더해 곱하고
    return cnt-1                    # 최소 1개는 입는다고 했으므로 전체 경우에서 아무것도 안 입는 경우 1을 빼준다



# 다른 사람 코드
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes]) #collections 의 Counter 함수를 이용해서 kind의 갯수를 세어
                                                    #dictionary의 형태로 kind가 각각 몇개인지 반환해준다
                                                    
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
                                                               #reduce함수를 이용해서 연산을 해줄수 있는데
                                                               #맨뒤의 1은 초깃값으로 설정된 1이고
                                                               #cnt dictionary에 저장되어있는 value들을 가져와
                                                               #갯수 + 1 (안입는 경우는 생각)하여 x에 곱해나가준다
                                                               #그리고 마지막으로 전체값에 -1을 해준다
    return answer

# 출처 : https://chibychi.blogspot.com/2019/07/44-python.html
