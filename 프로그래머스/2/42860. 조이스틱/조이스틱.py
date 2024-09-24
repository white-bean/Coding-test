def solution(name):
    answer = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # N = 13
    if name == 'A'*len(name): return 0
    leftright = len(name)-1 # 좌우로 이동할 수 있는 최대값
    for i, s in enumerate(name):
        answer += min(alphabet.index(s), 26 - alphabet.index(s)) # 상하
        notA = i + 1 # A가 아닌 알파벳 위치
        while (notA < len(name)) and (name[notA] == 'A'): notA += 1
        leftright = min(leftright, i + len(name) - notA + min(i, len(name) - notA))
    answer += leftright
    return answer