# 1. 2*2 찾고, 제거 좌표 저장 
# 2. 저장한 좌표 제거하면서 갯수 카운트
# 3. 빈 공간에 블록 드랍(떨어지기) 
# 1 후에 제거 좌표가 없다면 프로그램 종료 

# 2*2 찾기 알고리즘 
    # flood fill 부적합
    # 현재 좌표를 기준으로 우, 하, 우하가 같은 것인지 확인 => 마지막 열, 마지막 행까지는 탐색 돌면 안됨 

# 블록 드랍 알고리즘 
    # 탐색 방향
        # for 한 열 
            # for 현재 열의 한 행 (맨 밑 행부터 위로 탐색)
    # 빈 공간이 있다면 그 윗 블록들을 한 행씩 밑으로 이동 
    
def solution(m, n, board):
    def print_board(): # 디버깅용 함수 
        for r in board:
            print(r)
        print()
        
    answer = 0
    
    # 현재, 우, 하, 우하
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]
    
    # board를 2차원 배열로 변경 
    for i in range(m):
        board[i] = list(board[i])
    
    while True: 
        # 2*2 찾기 
        remove_position = set([]) # 중복 방지 

        for i in range(m-1):
            for j in range(n-1):
                cur = board[i][j]
                
                if cur == '-':
                    continue
                    
                # 현재를 기준으로 우, 하, 우하 확인
                if cur == board[i][j+1] and cur == board[i+1][j] and cur == board[i+1][j+1]:
                    # 사방 좌표 저장 
                    for dir in range(4):
                        nr = i + dr[dir]
                        nc = j + dc[dir]
                        remove_position.add((nr, nc))

        # 제거할 블록이 없다면 탈출 
        if not remove_position:   
            break

        # 블록 제거 
        for i, j in remove_position:
            board[i][j] = " "
            # 제거 카운트 
            answer += 1

        # 블록 드랍 
        for i in range(n): # 열
            for j in range(m-1, -1, -1): # 행 
                if board[j][i] == " ":
                    # 블록이 채워질 때까지 윗행 아래로 당기기 
                    while True:
                        if board[j][i] != " ":
                            break
                            
                        # 범위: 현재 열의 윗행 ~ 첫행까지 
                        for k in range(j-1, -1, -1):
                            board[k+1][i] = board[k][i]
                        board[0][i] = '-'

    return answer