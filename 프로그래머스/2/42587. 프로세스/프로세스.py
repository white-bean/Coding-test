from collections import deque
def solution(priorities, location):
    pr = deque(priorities)
    max_num = max(pr);ans=1
    while pr:
        n = pr.popleft()
        if n < max_num: pr.append(n);location = len(pr)-1 if location - 1 < 0 else location - 1
        else: 
            if location == 0: return(ans)
            else: max_num = max(pr); ans+=1; location -= 1
    return 0