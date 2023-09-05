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
    # 0 ~ k까지 말 이동 횟수에 따라서 경로 종류를 나눔
    visited = [[[0] * (k+1) for _ in range(W)] for _ in range(H)]

    q.append((sr, sc, 0))
    visited[sr][sc][0] = 1

    while q:
        # horse: 현재 지점까지의 말 이동 횟수 
        cr, cc, horse = q.popleft()

        if cr == H - 1 and cc == W - 1:
            return visited[cr][cc][horse] - 1

        for dir in range(12):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            nh = horse

            if 0 <= dir <= 7:
                # 말 이동 횟수가 최대치라면 말 이동 불가 
                if horse == k:
                    continue
                nh += 1

            # 조건
            # 범위 내, 미방문
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][nh]:
                # 장애물 여부 
                if not board[nr][nc]:
                    # 말 이동 횟수에 따른 경로를 삽입
                    q.append((nr, nc, nh))
                    # 말 이동 횟수에 따른 경로에 카운트를 삽입하여 방문 처리 
                    # 이번 턴에서 말 이동했다면 경로가 달라지는 것임
                    # ex. 현재지점까지는 '1회 이동' 경로로 왔는데 이번 턴에서 '2회 이동' 경로로 전환해야 함
                    # => '1회 이동' 경로에 지금까지의 카운트가 저장되어 있으니, 거기에서 1증가하여 '2회 이동'에 저장 
                    visited[nr][nc][nh] = visited[cr][cc][horse]+1

    return -1

k = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

print(bfs(0, 0))