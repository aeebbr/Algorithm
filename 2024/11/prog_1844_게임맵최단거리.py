from collections import deque
def solution(maps):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    n, m = len(maps), len(maps[0])
    
    def bfs():
        q = deque([(0, 0, 1)])
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        
        while q:
            cr, cc, cnt = q.popleft()
            
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
            
                if (nr, nc) == (n-1, m-1): # 성공 
                    return cnt + 1
            
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    if maps[nr][nc] == 1:
                        q.append((nr, nc, cnt+1))
                        visited[nr][nc] = True
        
        return -1
    
    return bfs()
