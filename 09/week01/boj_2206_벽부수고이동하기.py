# 최단 경로 => BFS
# bfs 탐색하면서 벽 부순 경로 / 부수지 않은 경로로 나눠서 가다가, 제일 먼저 목적지에 도착한 경로에서 종료 
# 칸마다 현재 경로까지 벽 부쉈는지 여부를 저장해야 함 

# 이동하다가 벽을 만났을 때, 어차피 벽을 안 부수면 못 감 
# 벽을 부수지 않고 우회하는 법 = 인접한 다른 방향으로 가는 것 = 다른 방향의 경로를 내는 것 

# 특수한 경우에 따라 경로가 나뉘는 경우라면 3차원 방문 배열을 써야 함 
# [r][c][0] => 벽 부수지 않은 경로 
# [r][c][1] => 벽 부순 경로 
# 이동하다가 벽을 만나면, 현재 경로가 벽 부수지 않은 경로인지 확인 => 벽 부수기 

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    q = deque()
    # (시작 위치, 경로 종류)
    q.append((sr, sc, 0))

    # 벽 부술 기회에 따른 각 경로에 이동 횟수 카운트하며 방문 처리 
    # [벽 부술 기회 여부]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[sr][sc][0] = 1

    while q:
        # 현재 지점, 경로 종류 
        cr, cc, route = q.popleft()

        if (cr, cc) == (N-1, M-1):
            # cnt는 이동할 때 증가, 도착지는 현재 지점이기 때문에 이미 이전 턴에서 증가하고 온 것임
            # => cnt 증가 없이 리턴
            return visited[cr][cc][route]

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < M:
                # 벽이고, 벽 부수지 않은 경로라면 부수기 
                if board[nr][nc] == 1 and route == 0:
                    # 벽 부쉈으니, 경로 1로 전환
                    q.append((nr, nc, 1))
                    # 벽 부순 경로에 방문 처리 
                    # 이 지점의 카운트는 벽 부수지 않은 경로의 현재 위치에 저장되어 있음 
                    visited[nr][nc][1] = visited[cr][cc][0] + 1

                # 빈 곳이라면 벽 부순 여부 상관 없음 
                # 어떤 경로든지 간에 미방문이라면 이동 
                elif board[nr][nc] == 0 and not visited[nr][nc][route]:
                    q.append((nr, nc, route))
                    visited[nr][nc][route] = visited[cr][cc][route] + 1

    return -1

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))