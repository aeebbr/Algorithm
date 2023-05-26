# 탐색하다가 바둑알이 나오면 바둑알 카운트 시작
# 발견한 바둑알을 기준으로 사방, 대각선으로 탐색

# 카운트
# 카운트가 5라면, 육목 확인

board = []

# 사방 
# 우 우하 하 좌하 좌 좌상 상 우상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(19):
    board.append(list(map(int, input().split())))

# for i in board:
#     for j in i:
#         print(j, end=" ")
#     print()
def findOmok(cr, cc):
    # 사방, 대각선 탐색
    for dir in dr:
        # 이동한 위치의 내용물
        nr = cr + dr[dir]
        nc = cc + dc[dir]


# 바둑알 찾기 
for i in range(len(board)):
    for j in range(len(board[i])):
        # 바둑알 발견 
        if not board[i][j] == 0:
            findOmok(i, j)


# 0 0 0
# 0 1 0
# 0 0 0