import sys 
from collections import deque
input = sys.stdin.readline

# 북 동 남 서 
# 상 우 하 좌 
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def on():
    # 청소하는 칸 개수 
    cnt = 0

    cr, cc, cd = sr, sc, sd

    while True:
        # 현재 칸 탐색
        # 현재 칸이 청소되지 않았다면 청소 
        if board[cr][cc] == 0:
            # 청소된 칸은 2로 갱신
            board[cr][cc] = 2
            # 청소 카운트 갱신
            cnt += 1

        # 사방 탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]    

            # 조건
            # 이동 지점이 범위 내인가
            # 이동 지점이 방문하지 않은 곳인가 
            # 이동 지점이 청소되지 않은 빈칸인가 
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    # 현재 방향에서 반시계 방향으로 90도 회전 
                    cd = (cd + 3) % 4

                    rr = cr + dr[cd]
                    rc = cc + dc[cd]

                    # 회전 지점의 앞 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
                    if board[rr][rc] == 0:
                        # 현재 지점 갱신
                        cr = rr
                        cc = rc

                    break
        # 사방 탐색 다 했는데도 청소되지 않은 빈칸이 없다면 
        else:
            # 후방 지점 
            br = cr - dr[cd]
            bc = cc - dc[cd]
            
            # 후진 조건
            if 0 <= br < N and 0 <= bc < M:
                # 빈 칸인가 
                if board[br][bc] == 0 or board[br][bc] == 2:
                    # 현재 지점 갱신
                    cr = br
                    cc = bc    
                    # 다음 지점으로 이동 
                    continue

            # 후진 안되면 작동 멈춤
            return cnt

# 입력
N, M = map(int, input().split())
sr, sc, sd = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(on())
