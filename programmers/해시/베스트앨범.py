# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.


def solution(genres, plays):
    dict={}
    for i in range(0, len(genres)):      
        if genres[i] in dict:
            dict[genres[i]]['plays'].append([plays[i], i])
            dict[genres[i]]['plays_sum']+=plays[i]
        else:
            dict[genres[i]]={}
            dict[genres[i]]['plays']=[[plays[i], i]]
            dict[genres[i]]['plays_sum']=plays[i]

    #print(dict)
    dict2=dict.items()
    #print(dict2)
    dict3=sorted(dict2, key=lambda x: x[1]['plays_sum'], reverse=True)

    answer=[]
    for i in range(0, len(dict3)):
        dict4=dict3[i][1]['plays']
        print(dict4)
        dict4.sort(reverse=True)
        print(dict4)
    
        for j in range(0, 2):
            answer.append(dict4[j][1])
            
    print(answer)
    return answer

# 최대한 줄여보려하였으나 계속 런타임에러가 남
# 아래 코드랑 비교해봤을 때 다른 점은 처음 딕셔너리 만들 때 나눠서 만드냐 합쳐서 만드냐인데...
# 정렬하는 과정에서 시간소모가 큰 것 같다는 추측!
    
    
    
# 다른 사람 
def solution(genres, plays): 
    answer = [] 
    genre_total_play = {} 
    genre_dic = {} 
    for i in range(len(genres)): 
        if genres[i] not in genre_dic.keys(): 
            genre_dic[genres[i]] = [(plays[i], i)] 
            genre_total_play[genres[i]] = plays[i] 
        else: 
            genre_dic[genres[i]].append((plays[i], i)) 
            genre_total_play[genres[i]] = genre_total_play[genres[i]] + plays[i] 

    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True) 
    print(sorted_total_play) 
    for key in sorted_total_play: 
        play_list = genre_dic[key[0]] 
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1])) 
        for i in range(len(play_list)): 
            if i == 2: 
                break 
            answer.append(play_list[i][1]) 
            
    return answer
