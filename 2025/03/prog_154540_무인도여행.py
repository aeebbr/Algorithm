'''
한 덩어리(무인도)를 찾아라 
'''
from collections import deque
def solution(maps):
    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = True
        cnt = int(maps[sr][sc])
        
        while q:
            cr, cc = q.popleft()
            
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                
                # 조건: 전체 범위 내일 것, 숫자일 것, 방문하지 않은 곳일 것
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc].isdigit():
                    if not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
                        cnt += int(maps[nr][nc])                        
        return cnt 
    
    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j].isdigit() and not visited[i][j]:
                total = bfs(i, j)
                answer.append(total)

    if answer:
        return sorted(answer)
    else:
        return [-1]