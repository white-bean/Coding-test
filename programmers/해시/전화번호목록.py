# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.



def solution(phone_book):
    phone_book.sort()

    for i in range(0, len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return True




# 다른 사람 풀이 1

def solution(phone_book):
    answer = True 
    phone_book.sort() 
    for i in range(len(phone_book)-1): 
        if phone_book[i] in phone_book[i+1]:    # 'in' 명령어 기억하자! 꽤 효율적인듯
            answer = False 
            break 
            
    return answer


# 다른 사람 풀이 2
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# zip함수로 바로 옆 원소 묶음
# p2.startswith(p1) : 문자열 p1이 문자열 p2 맨 앞에 있다면 true, 아니면 false


# 다른 사람 풀이 3
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

# hash_map은 {'119': 1, '97674223': 1, ' 1195524421': 1}이 된다.
# 첫 번째 반복의 phone_number= "119"이고 number="1", temp="1"이고, temp자체가 hash_map에 없으므로 다음 반복
# number="1", temp="11"이 되는데 11도 hash_map에 없음
# number="9", temp="119가 되는데 119는 hash_map에 있음, 그러나 temp="119"와 phone_number ="119"와 같으므로 다음 반복
# 쭈우욱 반복해서 phone_number = "1195524421"일 때 temp = "119"까지 반복하면 조건이 만족해서 answer=False로 뜰 것이다.
# 출처 : https://assaeunji.github.io/python/2020-05-08-pgphone/
