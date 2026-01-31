# bfs
# cnt가 작은 것부터 탐색해야 함 
# 같은 수가 들어가면 안됨 => 중복 확인(방문 처리)
from collections import deque
def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = [False for _ in range(y+1)]
    visited[x] = True
    
    while q:
        num, cnt = q.popleft()
        
        if num == y:
            return cnt
        
        for i in range(3):
            if i == 0: 
                tmp = num * 3
            elif i == 1:
                tmp = num * 2
            else:
                tmp = num + n                
                
            if tmp <= y and not visited[tmp]:
                q.append((tmp, cnt+1))
                visited[tmp] = True
    
    return -1