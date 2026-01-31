'''
동작: 제거 -> 드랍 

2*2 덩어리 찾기 
    1. 모든 지점 탐색 
    2. 현재 지점 기준으로 우, 하, 우하 확인해서, 세 지점이 현재와 같은 문자라면 성공 
    

'''
from collections import deque
def solution(m, n, board):
    def print_board(board):
        for b in board:
            print(b)
    
    # 우 하 우하
    dr = [0, 1, 1]
    dc = [1, 0, 1]
    

        
    def get_remove_block():
        remove_position = []
        
        # 제거할 위치 찾기 
        for cr in range(m-1):
            for cc in range(n-1):
                cur = board[cr][cc]
                
                if cur == ' ':
                    continue
                
                tmp = [(cr, cc)]

                for d in range(3):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if board[nr][nc] != cur:
                        break

                    tmp.append((nr, nc))

                # 2*2 찾음 
                else:
                    remove_position.extend(tmp)

        return sorted(list(set(remove_position)), key = lambda x: x[0])
    
    def remove_block(block):
        for r, c in block:
            for j in range(r-1, -1, -1):
                board[r][c] = board[j][c]
                board[j][c] = ' '
                r = j
            
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        block = get_remove_block()
        
        if len(block) == 0:
            break
            
        remove_block(block)
        answer += len(block)
    
    return answer