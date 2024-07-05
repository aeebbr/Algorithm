def solution(board, h, w):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    color = board[h][w]
    n = len(board)
    answer = 0
    
    for dir in range(4):
        cr = h + dr[dir]    
        cc = w + dc[dir]
        
        if 0 <= cr < n and 0 <= cc < n and board[cr][cc] == color: 
            answer += 1
    
    return answer