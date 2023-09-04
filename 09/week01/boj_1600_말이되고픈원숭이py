import sys
input = sys.stdin.readline
from collections import deque

# 말의 방향, 우하좌상
dr = [-2, -2, -1, -1, 1, 1, 2, 2, 0, 1, 0, -1]
dc = [-1, 1, -2, 2, -2, 2, -1, 1, 1, 0, -1, 0]

def bfs(sr, sc):
    # 큐 초기화 
    q = deque()
    # 방문배열 초기화 
    # 0 ~ k까지 
    visited = [[[0] * (k+1) for _ in range(W)] for _ in range(H)]

    q.append((sr, sc, 0))
    visited[sr][sc][0] = 1

    while q:
        cr, cc, horse = q.popleft()

        if cr == H - 1 and cc == W - 1:
            return visited[cr][cc][horse] - 1

        for dir in range(12):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            nh = horse

            if 0 <= dir <= 7:
                # horse > k로 하면 말 증가할 수 없음 
                if horse >= k:
                    continue
                nh += 1

            # 조건
            # 범위 내, 미방문
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][nh]:
                # 장애물 여부 
                if not board[nr][nc]:
                    q.append((nr, nc, nh))
                    visited[nr][nc][nh] = visited[cr][cc][horse]+1

    return -1

k = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

print(bfs(0, 0))