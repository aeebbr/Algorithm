# 5 * 5의 각 칸을 0 ~ 24로 넘버링
    # r = num / 5
    # c = num % 5

# 0 ~ 24에 해당하는 각 좌표 7개를 중복 X, 조합 
# 조합하면서 인자로 S, Y의 수를 누적, Y의 개수가 4를 넘어가면 해당 조합 실패, return 
# 조합하고 나서, bfs 돌리면서 조합한 좌표들이 한 덩어리인지 체크 

import sys 
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = 0

# 조합이 모두 근접한 것들인지 체크 
# 조합의 첫번째 칸을 기준으로 조합에 있는 것 중에서 근접한 좌표로 퍼져나가기 
def bfs(sel):
    global answer

    q = deque()
    visited = [[False] * 5 for _ in range(5)]

    r, c = sel[0]
    visited[r][c] = True
    q.append((r, c))

    # 인접 좌표의 총 개수 
    cnt = 1

    while q:
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                # 인접 좌표가 sel 안에 있어야 함
                if (nr, nc) in sel:
                    q.append((nr, nc))
                    visited[nr][nc] = True

                    cnt += 1
                
    if cnt == 7:
        answer += 1

# 조합 
def recur(idx, sel, total_cnt, s_cnt):
    # 종료 조건
    # 실패: Y가 4개 이상이면 S는 최소 개수를 맞출 수 없으므로 실패 
    if total_cnt - s_cnt >= 4:
        return 
    # 성공
    if len(sel) == 7:
        # 이 조합이 한 덩어리인지 확인
        bfs(sel)
        return 

    for i in range(idx, 25):
        # 좌표 
        r = i // 5
        c = i % 5

        sel.append((r, c))
        if board[r][c] == 'S':
            s_cnt += 1

        recur(i + 1, sel, total_cnt+1, s_cnt)
        
        sel.pop()
        if board[r][c] == 'S':
            s_cnt -= 1

board = [list(input().rstrip('\n')) for _ in range(5)]

# 0 ~ 24 조합 
recur(0, [], 0, 0)
print(answer)

# import sys 
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# # 우 하 좌 상
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# def recur(cr, cc, total_cnt, s_cnt, visited):
#     # 종료(성공)
#     if total_cnt == 7:
#         if s_cnt >= 4:
#             print()
#             return 
#     # Y가 4개 이상이라면 종료(실패) 
#     if total_cnt - s_cnt >= 4:
#         return 

#     # 탐색 방향: 우, 하 
#     # 우, 하 방향으로만 탐색을 해서, 이전 턴에서 
#     for dir in range(4):
#         nr = cr + dr[dir]
#         nc = cc + dc[dir]

#         if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
#             if board[nr][nc] == 'S':
#                 s_cnt += 1
#             visited[nr][nc] = True

#             recur(nr, nc, total_cnt + 1, s_cnt, visited)

#             if board[nr][nc] == 'S':
#                 s_cnt -= 1
#             visited[nr][nc] = False

# board = [list(input().rstrip('\n')) for _ in range(5)]

# for i in range(5):
#     for j in range(5):
#         if board[i][j] == 'S':
#             visited = [[False] * 5 for _ in range(5)]
#             visited[i][j] = True
#             recur(i, j, 1, 1, visited)