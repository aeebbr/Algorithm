def solution(n):
    answer = []
    tri = []
    end_num = 0 # 채워야 하는 마지막 숫자 
    
    # 삼각형 틀 만들기 
    for i in range(1, n+1):
        end_num += i
        tmp = [0] * i
        tri.append(tmp)
        
    # 하, 우, 좌상
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    cr, cc = -1, 0
    dir = 0
    num = 1
    
    while True:
        # 마지막 숫자보다 크다면 종료  
        if num > end_num :
            break
            
        nr = cr + dr[dir]
        nc = cc + dc[dir]
        
        if 0 <= nr < n and 0 <= nc < len(tri[nr]) and tri[nr][nc] == 0:
            tri[nr][nc] = num
            cr, cc = nr, nc
            num += 1
            continue
                
        # 조건에 맞지 않다면 방향 바꾸기 
        dir += 1
        if dir > 2:
            dir = 0
    
    # 배열 합치기 
    for row in tri:
        answer.extend(row)
    
    return answer