# 최단 거리가 아니라, 잃는 금액이 최소인 경로

import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc, s_money):
    q = PriorityQueue()
    q.put((s_money, sr, sc))
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True  

    while q:
        c_money, cr, cc = q.get()

        if (cr, cc) == (N-1, N-1):
            return c_money
        
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                q.put((c_money+board[nr][nc], nr, nc))
                visited[nr][nc] = True

    return 0

test_case = 0
while True:
    test_case += 1
    N = int(input())
    if N == 0: break 
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f"Problem {test_case}: {bfs(0, 0, board[0][0])}")
