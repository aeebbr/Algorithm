# 멈출 때까지 같은 방향으로 직진 
from collections import deque
def solution(board):
    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc, 0))
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[sr][sc] = True
        
        while q:
            cr, cc, cnt = q.popleft()
            
            if board[cr][cc] == 'G':
                return cnt
            
            for d in range(4):
                nr, nc = cr, cc
                
                # 멈출 때까지 직진 
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    
                    # 조건: 전체 범위 내일 것, 장애물이 아닐 것('G'도 가능)  
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'D': 
                        continue
                    else:
                        nr -= dr[d]
                        nc -= dc[d]
                        
                        if not visited[nr][nc]:
                            q.append((nr, nc, cnt+1))
                            visited[nr][nc] = True
                            
                        break
                
        return -1 
    
    answer = 0
    N = len(board)
    M = len(board[0])
    
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    flag = False
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                answer = bfs(i, j)    
                flag = True
                break
        if flag:
            break 
            
    return answer