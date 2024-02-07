# dfs로 풀이 
# 연결되어 있는 하나의 덩어리 개수와 각 덩어리의 칸 수 카운팅하는 문제 

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 단지 리스트 
answer = []

def dfs(cr, cc):
    global answer
    global board

    answer[-1] += 1 

    # 현재 위치 방문 처리 
    board[cr][cc] = 2

    for dir in range(4):
        nr = cr + dr[dir]
        nc = cc + dc[dir]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 1:
            dfs(nr, nc)

N = int(input())

board = []
home = []

# 입력 받으면서 집이 있는 위치를 저장해두기 
for i in range(N):
    row = list(map(int, input()))
    board.append(row)

    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
            
# 각 집 위치를 시작으로 dfs 탐색
for r, c in home:
    if board[r][c] == 1:
        answer.append(0)
        dfs(r, c)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)