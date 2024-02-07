# dfs로 풀이 

import sys 
sys.setrecursionlimit(10**4)
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def melt(board):
    # 빙산과 맞닿은 바다 개수 
    sea_with_ice = deque([])

    # 빙산별로 맞닿은 바다 개수 체크 
    # 한 빙산 기준 사방의 인덱스에 접근하니까 범위를 1 ~ N - 1
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] != 0:
                # 현재 빙산 기준 사방의 값을 저장 
                # 우 하 좌 상
                check_list = [board[i][j+1], board[i+1][j], board[i][j-1], board[i-1][j]]
                # 그 중 빙산의 개수만 저장
                sea_with_ice.append(check_list.count(0))

    # 빙산 높이 줄이기(빙산 녹는)
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                arround = sea_with_ice.popleft()
                board[i][j] -= arround

                # 빙산 최소 높이는 0으로 
                if board[i][j] < 0:
                    board[i][j] = 0

    return board

def dfs(cr, cc, visited, board):
    # 방문 처리 
    visited[cr][cc] = True

    # 사방 탐색
    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if board[nr][nc] != 0:
                dfs(nr, nc, visited, board)

# 입력 
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    # 이번 년도 시작

    # 빙산 덩어리 수 
    big_ice_cnt = 0
    visited = [[False] * M for _ in range(N)]

    # 빙산의 덩어리 수 체크 
    # 모든 좌표를 돌면서 빙산인 곳은 탐색
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] != 0:
                dfs(i, j, visited, board)
                big_ice_cnt += 1
    
    # 빙산 덩어리가 두쪽 이상인지 체크 
    if big_ice_cnt > 1:
        print(year)
        break
    else:
        year += 1
        # 녹는 빙산 구하기 
        board = melt(board)
