def solution(dirs):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    direction = {
        "R": 0, "D": 1, "L": 2, "U": 3
    }
    
    # board = [[0] * 11 for _ in range(11)] 이런 2차원 배열이 있다고 가정하고 이동
    cr, cc = 5, 5 # 원점: (5, 5)
    path = set()
    
    for d in dirs:
        d = direction[d]
        nr = cr + dr[d]
        nc = cc + dc[d]
        
        if 0 <= nr < 11 and 0 <= nc < 11:
            # 길을 양방향으로 저장
            path.add(((cr, cc), (nr, nc)))
            path.add(((nr, nc), (cr, cc)))
            
            cr, cc = nr, nc
    
    return len(path) // 2