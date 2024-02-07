# 통로 -> 레버 -> 출구 
# 레버 전에 출구 만나면 나갈 수 없음(레버 전에 출구 먼저 지나갈 수 있음)
# 3차원 방문 배열로 경로 두 개 
    # 0: 레버 전 
    # 1: 레버 후 
from collections import deque

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    def bfs(sr, sc):
        q = deque()
        visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
        # 시작점, 경로 종류 
        q.append((sr, sc, 0))
        # 시작을 1로 카운트 
        visited[sr][sc][0] = 1
        
        while q:
            cr, cc, route = q.popleft()
            
            # 목적지 만났다면: 레버 만난 후일 때만 목적지로 
            if maps[cr][cc] == 'E' and route == 1:
                return visited[cr][cc][route] - 1
                
            for dir in range(4):
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][route]:
                    # 목적지는 레버를 만나기 전이라면 통로에 불과하고, 레버 만난 후에야만 목적지로의 의미를 가짐
                    # 레버 만난 후라면 통로와 출발지도 한 번 더 갈 수 있음 
                    if maps[nr][nc] == 'O' or maps[nr][nc] == 'E' or maps[nr][nc] == 'S':
                        q.append((nr, nc, route))
                        visited[nr][nc][route] = visited[cr][cc][route] + 1
                    # 레버 만났다면: 레버 만나기 전 경로일 때만 지나가기 
                    # 레버 만난 후 경로로 전환하기 
                    elif maps[nr][nc] == 'L' and route == 0:
                        q.append((nr, nc, 1))
                        visited[nr][nc][1] = visited[cr][cc][route] + 1
                        
            # for i in range(len(visited)):
            #     print(visited[i])
            # print()
                        
        return -1 
                    
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                return (bfs(i, j))
    