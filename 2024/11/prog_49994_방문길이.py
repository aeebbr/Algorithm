def solution(dirs):
    # 상 하 우 좌 
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    dir_idx = {
        'U': 0, 
        'D': 1, 
        'R': 2, 
        'L': 3
    }
    
    cr, cc = 5, 5 # 시작점
    visited = set()
    
    for d in dirs:
        idx = dir_idx[d]
        nr = cr + dr[idx]
        nc = cc + dc[idx]
        
        # 5, 5 => 4, 5로 이동했다면 (5, 5, 4, 5), (4, 5, 5, 5)
        if 0 <= nr < 11 and 0 <= nc < 11:
            visited.add((cr, cc, nr, nc))
            visited.add((nr, nc, cr, cc))
            
            cr, cc = nr, nc
            
    return len(visited) // 2
