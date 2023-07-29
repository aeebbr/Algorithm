import sys 
from collections import deque
input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    # 큐 초기화 
    q = deque()
    # 방문 배열
    visited = [[False] * (M + 1) for _ in range(N + 1)]

    # 시작 지점, 초기 횟수 큐에 삽입 
    q.append([SR, SC, 0])
    visited[SR][SC] = True

    while q:
        # 큐에서 하나 꺼내기 
        cr, cc, cnt = q.popleft()

        if cr == FR and cc == FC:
            return cnt

        # 사방 탐색
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            # 조건 확인
            # 1) 범위 내(사각형 범위 고려해서)인지, 2) 방문하지 않았는지, 3) 빈 공간인지
            if 1 <= nr <= N and 1 <= nc <= M and 1 <= nr <= N - H + 1 and 1 <= nc <= M - W + 1 and not visited[nr][nc]:
                isWall = False

                for r, c in wall:
                    # 벽이 사각형 범위 내에 있는지 확인(시간 줄이기!!!)
                    if nr <= r < nr + H and nc <= c < nc + W:
                        isWall = True  
                        break
                
                # 사각형의 모든 지점이 빈 곳이라면
                if not isWall:
                    q.append([nr, nc, cnt + 1])
                    visited[nr][nc] = True

    return -1

# 입력
N, M = map(int, input().split())
board = [[0] * (M + 1)]
wall = []

for i in range(N):
    row = [0]
    row.extend(list(map(int, input().split())))
    board.extend([row])

    for j in range(M + 1):
        if row[j] == 1:
            wall.append((i + 1, j))

H, W, SR, SC, FR, FC = map(int, input().split())

if SR == FR and SC == FC:
    print(0)
else:
    print(bfs())