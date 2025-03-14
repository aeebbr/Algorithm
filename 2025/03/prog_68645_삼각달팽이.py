'''
n = 1, 1까지
n = 2, 3까지 
n = 3, 6까지 
n = 4, 10까지, 
n = 5, 15까지, 
n = 6, 21까지, 

1. 모든 칸을 미리 만들기 
2. 방향키로 칸을 이동 
    1. 아래로 
    2. 아래 끝, 오른쪽으로 
    3. 오른쪽 끝, 왼쪽위로
    4. 왼쪽위 끝, 1 반복 
'''

def solution(n):
    # 하 우 좌상
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    answer = []
    tri = [] # 삼각 배열 
    limit = 0 # 마지막 숫자 
    cr, cc = -1, 0 # 현위치 
    d = 0 # 방향 
    cnt = 1 # 현숫자 
    
    # 0은 빈칸, -1은 칸이 아님 
    for i in range(1, n+1):
        tri.append([0 for _ in range(i)])
        limit += i
    
    while cnt <= limit:
        nr = cr + dr[d]
        nc = cc + dc[d]
        
        # 조건: 전체 범위 내여야, 빈칸이어야 
        if 0 <= nr < n and 0 <= nc < len(tri[nr]) and tri[nr][nc] == 0:
            tri[nr][nc] = cnt 
            cnt += 1
            cr, cc = nr, nc
        # 방향 전환 
        else:
            d += 1 
            if d == 3: d = 0 
    
    # 배열 합치기 
    for row in tri:
        answer.extend(row)
    
    return answer