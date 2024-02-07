# dfs로 풀이 

# 따질 수 있는 침수 높이: 1 ~ 그 배열의 최대값, 아무 지역도 침수되지 않을 경우
    # 1 이하 침수될 때의 경우
    # 2 이하 침수될 때의 경우 ~ 최대값까지 모두 따지기 

import sys 
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 안전 영역 최대 개수 
# 아예 침수되지 않는 경우에는 안전 영역이 1개이기 때문에 1로 초기화
max_safe_cnt = 1

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# limit: 침수 최대 높이 
def dfs(cr, cc, limit):
    # 현재 지점 방문 처리
    visited[cr][cc] = True

    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 침수 최대 높이보다 높을 때 
            if board[nr][nc] > limit:
                dfs(nr, nc, limit)

N = int(input())

# 최대 높이
board = [list(map(int, input().split())) for _ in range(N)]
highest = max(map(max, board))

for high in range(1, highest + 1):
    visited = [[False] * N for _ in range(N)]
    safe_cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > high and not visited[i][j]:
                dfs(i, j, high)
                safe_cnt += 1

    max_safe_cnt = max(max_safe_cnt, safe_cnt)

print(max_safe_cnt)
