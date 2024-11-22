from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    
    q = deque([(x, 0)])
    visited = [False] * (y+1)
    visited[x] = True
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == y: # 성공 
            return cnt 
            
        for i in range(3):
            if i == 0:
                tmp = cur + n
            elif i == 1:
                tmp = cur * 2 
            elif i == 2:
                tmp = cur * 3
            
            if tmp > y or visited[tmp]:
                continue
            
            q.append((tmp, cnt+1))
            visited[tmp] = True
    
    return -1