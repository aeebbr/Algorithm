from collections import deque

# 우 하 좌 상, 좌상, 우상, 좌하, 우하, 제자리 
dr = [0, 1, 0, -1, -1, -1, 1, 1, 0]
dc = [1, 0, -1, 0, -1, 1, -1, 1, 0]

def bfs(sr, sc, board):
    second = 0

    q = deque()
    q.append((sr, sc))

    while q:
        visited = [[False] * 8 for _ in range(8)]
        q_len = len(q)

        # 9번째 턴부터는 무조건 벽이 없는 상태 => 무조건 목적지 도달 가능 
        if second == 9:
            return 1

        for _ in range(q_len):
            cr, cc = q.popleft()

            if board[cr][cc] == '#':
                continue

            if cr == 0 and cc == 7:
                return 1

            for dir in range(9):
                nr = cr + dr[dir]
                nc = cc + dc[dir]

                # 조건 
                # 범위 내, 미방문
                # 빈칸 
                if 0 <= nr < 8 and 0 <= nc < 8 and not visited[nr][nc]:
                    # 현재 빈 칸이고, 이동해서도 빈 칸인 곳
                    if board[nr][nc] == '.':
                        q.append((nr, nc)) 
                        visited[nr][nc] = True

        # 벽 이동 
        # 다음 턴에서 쓸 board
        board.pop()
        board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

        # 1초 증가 
        # 이번 턴으로 증가하는 시간 
        second += 1

        # 8초 후에 성공에 관계없이 모든 벽 없어짐 => 아직 이번 턴의 실패 여부 알 수 없는 상태임 
        # => 벽이 없어졌다고 해서 성공한 것이 아님
        # 벽이 없어졌지만 성공했을 수도, 실패했을 수도 있음. while문을 나가야 실패 판정이 남 
        # while문을 나가지 않고 9번째 턴을 도는지가 중요! 
        '''
        (반례)
        ########
        ........
        ........
        ........
        ........
        ........
        ........
        ........
        ----------------------------------------------------------------
        (8번째 턴, 마지막 벽 한 줄)
        ........
        ........
        ........
        ........
        ........
        ........
        ........
        ########
        에서 살아남지 못해서 큐 비게 됨 => 실패 
        실패 여부에 상관 없이 1)벽 이동 로직 거치고 2)8초로 증가함 => 8번째 턴에서 7초로 시작하여 8초로 증가함

        <8초 ~ 9초인 9번째 턴을 시작했는지가 성공의 조건>
        7 ~ 8초인 8번째 턴을 마치면 성공 여부에 상관 없이 벽은 무조건 사라진 상태 
        * 성공했다면 9번째 턴으로 넘어갈 것이고, 
        * 실패했다면 8번째 턴에서 while문 종료 
        => 9번째 턴을 시작한다면 성공!
        '''

    return 0


board = [list(input()) for _ in range(8)]

print(bfs(7, 0, board))