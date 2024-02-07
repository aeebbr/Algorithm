# 육목 체크 
import sys 
input = sys.stdin.readline
from collections import deque

# 우 하 우하 좌하
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

N = 19
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * 19 for _ in range(19)]

for r in range(19):
    for c in range(19):
        cur = board[r][c]
        if cur != 0:
            # 모든 방향 탐색 
            for dir in range(4):
                cnt = 1
                nr = r
                nc = c
                
                # 현재 방향으로 오목 탐색 
                for i in range(5):
                    nr += dr[dir]
                    nc += dc[dir]

                    if 0 > nr or nr >= N or 0 > nc or nc >= N or cur != board[nr][nc]:
                        # 되돌리기 
                        nr -= dr[dir]
                        nc -= dc[dir]
                        break

                    cnt += 1

                if cnt == 5:
                    # 반대 방향으로 육목 확인 
                    tr = r - dr[dir]
                    tc = c - dc[dir]

                    # 육목이면 다음 방향으로 패스 
                    if 0 <= tr < N and 0 <= tr < N and cur == board[tr][tc]:
                        continue

                    # 승부 
                    print(cur)

                    if dir == 3:
                        print(nr+1, nc+1)
                    else:
                        print(r+1, c+1)
                    exit()
                
print(0)
                        
