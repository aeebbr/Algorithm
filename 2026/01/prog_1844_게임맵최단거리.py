# bfs
from collections import deque
def solution(maps):
    # 우 하 좌 상 
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0, 0, 1))

    while q:
        cr, cc, cnt = q.popleft()
        
        if (cr, cc) == (n-1, m-1):
            return cnt

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            # 칸이 1일 것, 방문하지 않은 곳일 것, 범위 내일 것 
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1:
                    q.append((nr, nc, cnt+1))
                    maps[nr][nc] = 0
                        
    return -1