# bfs로 이동한 경로('#')를 탐색하며 각 위치에서의 방향을 저장
# 저장한 방향을 토대로, 어떤 명령어를 썼는지 유추 

import sys
input = sys.stdin.readline
from collections import deque

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
directions = ['>', 'v', '<', '^']

def check(r, c):
    # 인접 지점 중에서 #이 있는 곳의 개수 
    cnt = 0

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '#':
            cnt += 1

    if cnt > 1:
        return False
    else:
        return True

def bfs(r, c):
    # 이동 경로 
    path = deque()
    q = deque()

    q.append((r, c))
    visited = [[False] * W for _ in range(H)]
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()

        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                if board[nr][nc] == '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    # 방향의 인덱스 저장 
                    path.append(dir)

    return path 

H, W = map(int, input().split())

sharp_list = []
ans = []

board = []
for i in range(H):
    row = list(input().rstrip('\n'))
    board.append(row)
    for j in range(W):
        if row[j] == '#':
            sharp_list.append((i, j))
              
for r, c in sharp_list:
    # 이 때, 시작 지점은 반드시 한 방향으로만 출발했을 것
    # 여러 방향으로 갔다면, 시작 지점에서 1번 방향으로 끝까지 쭉 갔다가, 다시 시작 지점으로 되돌아와서 2번 방향으로 가야하니 명령의 개수가 최소가 될 수 없음)
    # .......###....
    # .........#....
    # .#####...###..
    # 이 경우, (0, 9)에서 시작하려면 상, 하 두 가지 방향으로 왔다갔다 해야 함
    # => 인접한 사방 중, #이 하나만 있는 곳이 시작 지점으로 적합 
    if check(r, c):
        path = bfs(r, c)

        # 탐색 끝, 
        print(r + 1, c + 1)

        # 첫번째 이동 방향(시작 좌표에서 두번째 좌표로 이동하는)
        cur = path.popleft()
        print(directions[cur])
        
        # 두 칸 전진한 것인지 알기 위한 이동 카운트  
        # 첫번째 이동 방향이 이미 큐에서 나왔으니 해당 방향을 포함해서 1로 초기화 
        cnt = 1

        # 모든 경로 탐색하며 각 경로에서 쓰인 명령어 찾기 
        # 시작 방향 pop 했으므로 두번째 방향부터 탐색
        for next in path:
            # 현재 방향과 다음 방향이 같다면, A인지(같은 방향으로 두 칸 전진한 것) 체크 
            if cur == next:
                cnt += 1

                # 회전 다음에는 반드시 전진(전진은 무조건 두 칸씩) => 
                if cnt % 2 == 0:
                    ans.append('A')
                    # 이동 카운트 초기화 
                    cnt = 0

            else:
                # 다음 방향이 현재 방향보다 왼쪽 인덱스(작다면)이라면 => 왼쪽으로 회전한 것 
                if next < cur:
                    # 예외: 상에서 오른쪽으로 회전한 경우 
                    if cur == 3 and next == 0:
                        ans.append('R')
                    else:
                        ans.append('L')
                else:
                    # 예외: 우에서 왼쪽으로 회전한 경우 
                    if cur == 0 and next == 3:
                        ans.append('L')
                    else:
                        ans.append('R')

                # 현재 방향 갱신 
                cur = next
                cnt += 1

        print(''.join(ans))
        break
