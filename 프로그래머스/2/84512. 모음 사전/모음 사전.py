from itertools import product
def solution(word):
    answer = 0
    tmp = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        for a in product(tmp, repeat=i):
            dictionary.append(''.join(a))
    dictionary.sort()
    return dictionary.index(word)+1