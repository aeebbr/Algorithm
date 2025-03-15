'''
이동경로: 시작지점 -> 레버 -> 출구 

방문 처리를 어떻게 할 것인가? 
1. bfs1: 시작지점 -> 레버: 방문처리 
2. bfs2: 레버 -> 출구: 이전의 방문처리를 초기화하고 다시 방문처리 
'''
from collections import deque
def solution(maps):
    def bfs(start, target):
        sr, sc = start
        q = deque()
        q.append((sr, sc, 0)) # (행, 열, 카운트)
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[sr][sc] = True
        
        while q:
            cr, cc, cnt = q.popleft()
            
            if maps[cr][cc] == target:
                return cnt
            
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                
                # 조건: 전체 범위 내일 것, 통로일 것, 방문하지 않았을 것 
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 'X':
                    if not visited[nr][nc]:
                        q.append((nr, nc, cnt+1))
                        visited[nr][nc] = True
        
        return -1
        
    answer = 0
    
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    N = len(maps)
    M = len(maps[0])
    
    S, L = (-1, -1), (-1, -1)
    
    # 시작지점, 레버 찾기 
    flag = False
    for i in range(N):
        for j in range(M):
            if S != (-1, -1) and L != (-1, -1):
                flag = True
                break
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
        if flag:
            break
            
    answer += bfs(S, 'L')
    if answer == -1:
        return -1
    
    tmp = bfs(L, 'E')
    if tmp == -1:
        return -1
    answer += tmp
    
    return answer