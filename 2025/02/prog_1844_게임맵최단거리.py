# 전형적인 bfs 문제 
from collections import deque
def solution(maps):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc, 1)) # 출발지부터 1로 카운트 함 
        visited = [[False for _ in range(M)] for _ in range(N)]
        
        while q:
            cr, cc, cnt = q.popleft()
            
            if cr == 0 and cc == 0:
                return cnt                
            
            # 사방으로 이동 
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                
                # 조건: 전체 범위를 벗어나지 않아야, 위치의 값이 1이어야, 이전에 방문하지 않은 곳이어야 
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1:
                    if not visited[nr][nc]:
                        q.append((nr, nc, cnt+1))
                        visited[nr][nc] = True
                    
        return -1
        
    N = len(maps)
    M = len(maps[0])
    
    return bfs(N-1, M-1)