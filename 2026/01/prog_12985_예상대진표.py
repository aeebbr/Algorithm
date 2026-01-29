# 구해야 하는 것: A와 B가 만나는 라운드 번호 
# (4), (7)
# 1, (4) / 5, (7)
# 1, 2 / 3, (4) / 5, 6 / (7), 8

# 타겟이 아닌 다른 참가자의 번호는 중요하지 않음 
from collections import deque
def solution(n,a,b):
    answer = 0
    q = deque()
    
    # 타겟: 1, 타겟아님: 0
    q = deque((0, 1) for _ in range(n)) # (타겟여부, 라운드)
    q[a-1], q[b-1] = (1, 1), (1, 1)
    
    while q:         
        left, right = q.popleft(), q.popleft()
        ln, lr = left
        rn, rr = right
        
        if ln == 1 and rn == 1:
            # A, B 만남 
            return lr
        elif ln == 0 and rn == 0:
            q.append((0, lr+1))
        else:
            q.append((1, lr+1))
            
    return 0