# 우하좌상
# 오른쪽으로 90도: 현재 방향에서 오른쪽으로 한 칸 
    # (dir % 4) + 1
# 왼쪽으로 90도: 현재 방향에서 왼쪽으로 한 칸 
    # (dir + 3) % 4
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution(command):
    answer = []
    
    # 초기 방향: 상 
    dir = 3
    cr = 0
    cc = 0
    for c in command:
        # 현재 명령어에 따라서 좌표 갱신 
        if c == 'R':
            dir = (dir + 1) % 4  
        elif c == 'L':
            dir = (dir + 3) % 4            
        elif c == 'G':
            # 현 방향으로 한 칸 전진
            if dir == 1 or dir == 3:
                cr = cr + dr[dir] * - 1
            else:
                cr = cr + dr[dir]
            cc += dc[dir]            
        elif c == 'B':
            # 현재 방향으로 한 칸 후진 
            if dir == 1 or dir == 3:
                cr = cr - dr[dir] * - 1
            else:
                cr = cr - dr[dir]
            cc -= dc[dir]
                        
    return cc, cr