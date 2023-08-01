# dfs로 풀이 

# 각 빙산의 사방을 탐색해서 빙산별로 인접한 0의 개수를 저장 
# 모든 빙산의 탐색이 끝나면, 모든 빙산의 높이 깎기
# 깎고 나서 빙산의 덩어리 개수 확인하기 -> 하면서 빙산 좌표 갱신 -> 2개 이상이면 종료 -> 아니면 다음 년도로 

import sys 
import copy
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution(cr, cc, copy_arr):
    # 현재 빙산의 인접 0 개수 
    cnt = 0
    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        if 0 <= nr < N and 0 <= nc < M:
            # 0이라면 개수 갱신 
            if copy_arr[nr][nc] == 0:
                cnt += 1

    tmp = copy_arr[cr][cc] - cnt

    if tmp <= 0:
        board[cr][cc] = 0
    else:
        board[cr][cc] -= cnt

        # 빙산이 남아있다면 빙산 갱신
        ice.append((cr, cc))

# 빙산 덩어리, 남은 빙산 갱신
def ice_check(cr, cc):
    global ice_cnt
    global visited

    ice_cnt += 1
    visited[cr][cc] = True

    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if board[nr][nc] != 0:
                ice_check(nr, nc)

N, M = map(int, input().split())
board = []
ice = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        # 빙산 좌표 저장 
        if row[j] != 0:
            ice.append((i, j))

year = 0
while True:
    # 이번 년도 시작
    # 빙산 별로 인접해있는 0의 개수 
    sea = [[0] * M for _ in range(N)]

    copy_arr = copy.deepcopy(board)
    copy_ice = copy.deepcopy(ice)
    ice.clear()
    for r, c, in copy_ice:
        solution(r, c, copy_arr)  

    # 1년 경과 
    year += 1

    visited = [[False] * M for _ in range(N)]

    # 빙산의 첫 덩어리만 탐색
    ir, ic = ice[1]
    ice_cnt = 0
    ice_check(ir, ic)

    if ice_cnt != len(ice):
        print(year)
        exit(0)
    