# flood fill 아님! 
# 보드를 어떻게 구성? 
    # 문제의 격자 점 하나를 한 칸으로 간주 
    # 11 * 11
    # 하지만 실제 보드 필요 없음
# 방문 기록 어떻게? 
    # 방향은 중요하지 않고, 길이 중요함. a->b이든 b->a이든 a-b이면 됨 
    # => 양방향 모두 기록해서 set으로 중복 제거 후 2로 나누면 순수 카운트 나옴 
def solution(dirs):
    # 우 하 좌 상
    dic = {
        'R': 0, 
        'D': 1,
        'L': 2, 
        'U': 3
    }
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    visited = set()
    cr, cc = 5, 5
    
    for d in dirs:
        idx = dic[d]
        nr = cr + dr[idx]   
        nc = cc + dc[idx]
        
        # 범위 내인지 
        if 0 <= nr < 11 and 0 <= nc < 11:
            # 방문 기록 
            visited.add((cr, cc, nr, nc))
            visited.add((nr, nc, cr, cc))
            
            cr, cc = nr, nc
            
    return len(visited) // 2