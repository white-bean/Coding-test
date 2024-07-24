def check(key_idx, lock_idx, N, M):
    for i in range(M+N-1):
        for j in range(M+N-1):
            cnt = 0
            for x, y in key_idx:
                if [x+i, y+j] in lock_idx:
                    cnt += 1
                # 홈이 아닌데 lock 영역에 있는 경우(lock 영역에서 돌기 부분)
                elif (M-1 <= x+i <= M+N-2) and (M-1 <= y+j <= M+N-2):
                    cnt = 0
                    break
            if cnt == len(lock_idx): return True
    return False

def solution(key, lock):
    M = len(key); N = len(lock)
    key_idx = [] # key 좌표
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1: key_idx.append([i, j])
    lock_idx = [] # lock 홈 좌표
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0: lock_idx.append([i+M-1, j+M-1])
            
    tmp = [[0]*(2*M+N-2) for _ in range(2*M+N-2)] # window
    for i in range(N):
        tmp[M-1+i][M-1:M-1+N] = lock[i]
    
    if check(key_idx, lock_idx, N, M): return True
    else:
        for _ in range(3):
            for i, (x, y) in enumerate(key_idx):
                key_idx[i] = [y, M-1-x]
            if check(key_idx, lock_idx, N, M): return True
        
    return False