'''
노란칸 형태의 모든 경우의 수 
'''
def solution(brown, yellow):
    answer = []
    
    # 노란칸 개수 = m * n 
    for n in range(1, yellow):
        if yellow % n == 0:
            m = yellow // n
            
            if n > m:
                break
                
            # 갈색칸 개수 구하기 
            brown_cnt = ((m+2) * 2) + (n*2) 
            if brown_cnt == brown:
                return [m+2, n+2]
            
    return [3, 3] # yellow가 1일 때 