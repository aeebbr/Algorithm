def solution(brown, yellow):
    # 카펫은 항상 가로로 긴 직사각형이거나, 정사각형임
    # 갈색은 항상 1줄임 
    '''
    갈색 = (노랑가로*2) + (노랑세로*2) + 4
    
    노랑이 24라면, 
    1*24 => 2+48+4
    2*12 => 4+24+4
    3*8 => 6+16+4 = 26
    4*6 => 8+12+4 = 24 !!! brown과 일치 
    
    전체가로 = 노랑가로 + 2
    전체세로 = 노랑세로 + 2
    '''
    y_w, y_h = 1, 1
    
    # 약수 찾기 
    for n in range(1, yellow):
        if yellow % n == 0:
            y_h = n
            y_w = yellow // n
            
            # 현재의 노랑 배열이 brown과 일치하는지 확인 
            tmp_brown = y_h*2 + y_w*2 + 4
            if tmp_brown == brown:
                break
                
    # 전체 가로, 세로 찾기 
    return [y_w+2, y_h+2]