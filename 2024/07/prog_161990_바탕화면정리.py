def solution(wallpaper):
    answer = []

    '''
    1, 5
    2, 6
    2, 7
    3, 3
    3, 4
    4, 4
    
    r의 최소: 1
    r의 최대: 4
    c의 최소: 3
    c의 최대: 7
    => 시작점: (r의 최소, c의 최소): 1, 3
    => 끝점: (r의 최대, c의 최대): 4, 7 => 5, 8
    '''
    
    rows = []
    cols = []
    
    N, M = len(wallpaper), len(wallpaper[0])
    
    for r in range(N):
        for c in range(M):
            if wallpaper[r][c] == '#':
                rows.append(r)
                cols.append(c)
    
    answer.append(min(rows))
    answer.append(min(cols))
    answer.append(max(rows)+1)
    answer.append(max(cols)+1)
    
    return answer