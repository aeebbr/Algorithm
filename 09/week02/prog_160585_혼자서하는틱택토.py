# 규칙 
# 선공: O, 후공: X
# O와 X를 번갈아서 놓았는가? 
# 빙고 한 줄이 나왔는데도 말이 남아있는가? 
def solution(board):    
    blank_cnt = 0
    o_cnt = 0
    x_cnt = 0
    # 빈칸, O, X의 개수 카운트 
    for row in board:
        blank_cnt += row.count('.')
        o_cnt += row.count('O')
        x_cnt += row.count('X')
            
    # 빈 게임판인 경우 
    if blank_cnt == 9:
        return 1
    if o_cnt > x_cnt and o_cnt - x_cnt != 1:
        return 0
    if o_cnt < x_cnt:
        return 0
    
    # 빙고 여부 확인
    # o의 빙고라면: o가 한 개 더 많아야 함(O의 턴에서 끝나기 때문)
    # x의 빙고라면: o, x 개수가 같아야 함(X의 턴에서 끝나기 때문)
    isOBingo = False
    isXBingo = False
    
    # 모든 빙고 케이스를 탐색해야 함 
    # 가로 빙고 
    for row in board:
        if row == "OOO":
            isOBingo = True
        elif row == "XXX":
            isXBingo = True
        if isOBingo and isXBingo: break
    # 세로 빙고 
    if not (isOBingo and isXBingo):
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 'O':
                    isOBingo = True
                elif board[0][j] == 'X':
                    isXBingo = True
                if isOBingo and isXBingo: break
    # 대각선 빙고 
    if not (isOBingo and isXBingo):
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'O':
                isOBingo = True
            elif board[0][0] == 'X':
                isXBingo = True
        elif board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'O':
                isOBingo = True
            elif board[0][2] == 'X':
                isXBingo = True
    
    if isOBingo and o_cnt - x_cnt != 1:
        return 0
    elif isXBingo and o_cnt != x_cnt:
        return 0
    elif isOBingo and isXBingo:
        return 0
    
    return 1
