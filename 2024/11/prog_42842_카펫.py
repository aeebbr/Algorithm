def solution(brown, yellow):
    answer = []
    
    """
    1. 노랑 배치 찾기: 가로, 세로 찾기 
    2. 각 노랑이 갈색이랑 일치하는지 확인
    3. 총 길이 계산하기 
    """
    
    for col in range(1, yellow + 1): 
        if yellow % col == 0:
            row = yellow // col
            
        # 갈색 개수 = ((노랑가로 + 2) * 2) + (노랑세로 * 2) 
        cur_brown_cnt = ((row + 2) * 2) + (col * 2)
        if cur_brown_cnt == brown:
            # 카펫 가로, 세로 
            answer = [(row + 2), (col + 2)]
            break
    
    return answer