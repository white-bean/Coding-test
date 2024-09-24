from collections import deque
import copy

def solution(name):
    answer = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # N = 13
    if name == 'A'*len(name): return 0
    name = list(name)
    dx = [-1, 1]
    def bfs(alist, cnt, idx):
        queue = deque([(alist, cnt, idx)])
        while queue:
            alist, cnt, idx = queue.popleft()
            cnt += min(alphabet.index(alist[idx]), 26 - alphabet.index(alist[idx]))
            alist[idx] = 'A'
            if alist == ['A']*len(alist):
                return cnt
            for i in dx:
                new_idx = (idx + i) % len(alist)
                new_alist = copy.deepcopy(alist)
                queue.append((new_alist, cnt + 1, new_idx))
            
    return bfs(name, 0, 0)