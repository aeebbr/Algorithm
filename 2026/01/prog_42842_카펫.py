# 정사각형 혹은 가로로 긴 직사각형 
# 갈색은 무조건 테두리 1줄 

# 노란색 기준으로 생각하기: 노란색 개수로 만들 수 있는 경우의 수 찾고, 그게 갈색과 부합하는 경우 찾기 
# 노란색 24개라면, 
#   24*1, 12*2, 8*3
# 갈색은 yw*2 + yh*2 + 4
import math
def solution(brown, yellow):
#   노란색 모든 경우의 수 
    yh = 1
    limit = math.isqrt(yellow)
    
    while yh <= limit:
        if yellow % yh == 0:
            yw = yellow // yh
            
#           갈색과 맞춰보기 
            if brown == (yw*2 + yh*2 + 4):
                return [yw+2, yh+2]
                    
        yh += 1