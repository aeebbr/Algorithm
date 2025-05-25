'''
1. 모든 응시자 위치 저장하기 
2. 각 응시자의 거리 1인 칸 확인하기 
    거리 1 떨어진 칸에 다른 응시자 있으면 무조건 탈락(파티션 있을 공간 없기 때문)
3. 각 응시자의 거리 2인 칸 확인하기 
    거리 2 떨어진 칸에 다른 응시자 있으면 그 사이에 파티션 있는지 확인 
    이 때 거리 2는 직선 방향으로 2, 대각선 방향으로 1를 의미함 
    
    직선 방향에 다른 응시자가 있다면, 해당 방향으로 1칸 떨어진 곳에 파티션이 있는지 확인
    대각선 방향에 다른 응시자가 있다면, 그 사이로 1칸 떨어진 곳에 파티션 있는지 확인 
'''

def solution(places):
    answer = []
    
    # 거리 1 탐색용(우하좌상 직선 1칸)
    dirs1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 거리 2 탐색용(직선 2칸, 대각선 1칸)
    dirs2 = [(0, 2), (2, 0), (0, -2), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    # 각 방 탐색 
    for place in places:
        p_position = [] # 응시자 위치 정보
        is_success = True # 거리두기 성공, 실패 여부 
        
        # 응시자 위치 저장하기 
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_position.append((i, j))
                
        # 거리 1 탐색
        for cr, cc in p_position:
            # 현 위치에서 사방으로 거리 1에 다른 응시자 있는지 확인 
            for dr, dc in dirs1:
                nr = cr + dr
                nc = cc + dc
                
                # 조건: 범위 내 
                if 0 <= nr < 5 and 0 <= nc < 5:
                    # 다른 응시자가 있다면 거리두기 실패 
                    if place[nr][nc] == 'P':
                        is_success = False
                        break
            if not is_success:
                break
            
        # 거리 2 탐색 
        for cr, cc in p_position:
            for dr, dc in dirs2:
                nr = cr + dr
                nc = cc + dc
                
                # 조건: 범위 내 
                if not (0 <= nr < 5 and 0 <= nc < 5):
                    continue
                if place[nr][nc] != 'P':
                    continue 
                    
                # 다른 응시자가 있다면 파티션 확인하기 
                # dr이나 dc가 2라면 직선, 1이라면 대각선 
                if abs(dr) == 2:
                    # 두 응시자 사이의 중간 위치 
                    mid_r = (cr + nr) // 2
                    
                    if place[mid_r][cc] != 'X':
                        is_success = False
                        break
                elif abs(dc) == 2:
                    mid_c = (cc + nc) // 2
                    
                    if place[cr][mid_c] != 'X':
                        is_success = False
                        break
                # 대각선이라면 
                else:
                    # 두 방향 모두 확인해야 함 
                    # 한 방향이라도 파티션이 없으면 거리두기 실패 
                    if place[nr][cc] != 'X' or place[cr][nc] != 'X':
                        is_success = False
                        break
                        
            if not is_success:
                break

        answer.append(1 if is_success else 0)
                        
    return answer