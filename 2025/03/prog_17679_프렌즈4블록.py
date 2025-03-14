'''
1. 2*2 찾기
    - 현재 원소를 기준으로 우, 하, 우하 탐색. 모두 같은 값이라면 2*2 찾은 것임 
    - 제거 배열에 4 군데 인덱스 삽입 
2. 2*2 제거 및 윗 블록들을 내려서 제거된 공간을 채우기 
    - 제거 배열에 삽입된 모든 인덱스의 동일 열, 윗행을 아래로 1칸씩 내리기 
    - 윗 블록부터 제거, 밑 블록부터 내리기 
'''
def solution(m, n, board):
    # def print_board(board):
    #     for row in board:
    #         print(row)
    #     print()
    
    def find_two_two_block():
        # 탐색 범위는 [0][0] 부터 [m-1][n-1]까지임
        for cr in range(m-1):
            for cc in range(n-1):
                cur = board[cr][cc]
                if cur == ' ':
                    continue

                tmp_block = [(cr, cc)]
                # 주위 우, 하, 우하 탐색하기 
                for d in range(3):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    # 조건: board 범위를 벗어나지 않아야, 같은 블록이어야 
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == cur:
                        tmp_block.append((nr, nc))

                if len(tmp_block) == 4:
                    two_two_block.extend(tmp_block)
                    
        if len(two_two_block) == 0:
            return False
        
        return True
    
    def remove_block():
        for i in range(len(two_two_block)):
            r, c = two_two_block[i]

            # 범위: 동일열, 윗행(r-1에서부터 0까지), 밑 블록부터 내리기 위해 r-1부터 0 순서로 탐색 
            for j in range(r-1, -1, -1):
                board[r][c] = board[j][c]
                board[j][c] = ' '
                r, c = j, c
    
    # 우 하 우하
    dr = [0, 1, 1]
    dc = [1, 0, 1]
    
    answer = 0
    two_two_block = []
    
    # board 열 쪼개기 
    for i in range(m):
        board[i] = list(board[i])
        
    while True:
        # 2*2 블록 찾기 
        if not find_two_two_block(): # 2*2 블록이 없으면 탈출 
            break
                    
        # 중복 블록 제거, 정렬(행 오름차순, 윗행에 있는 블록부터 제거)
        two_two_block = sorted(list(set(two_two_block)), key = lambda x: x[0])
        answer += len(two_two_block) # 지워지는 블록 개수 누적 

        # 2*2 블록 제거 
        remove_block()

        # 배열 초기화 
        two_two_block = []
    
    return answer