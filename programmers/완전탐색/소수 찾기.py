# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import permutations
import math

def is_prime_number(x): # 소수 구하는 함수
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    alist=list(numbers)
    b=[]
    for i in range(1, len(alist)+1): 
        blist=list(map(''.join, permutations(alist, i)))  # permutations 함수 이용해 모든 순열 구하기
        for j in blist:
            b.append(j)

    alist = list(set([int(x) for x in b]))  # set을 이용해 중복 제거
    
    for num in alist:
        if num >= 2 and is_prime_number(num)==True: # 2보다 크거나 같은 수 중 소수인 수 
            answer+=1
            
    return answer
