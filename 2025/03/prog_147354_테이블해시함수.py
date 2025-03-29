'''
1. 정렬: col번째 컬럼을 기준으로 각 튜플을 정렬
2. 2번부터는 row_begin부터 row_end까지의 행만 취급함 
'''
def solution(data, col, row_begin, row_end):
    answer = -1
    
    # 정렬 
    data = sorted(data, key = lambda x: [x[col-1], -x[0]])
    
    for i in range(row_begin-1, row_end):
        total = 0
        
        # data[i] 탐색 
        for j in data[i]:
            total += j % (i+1) 
        
        # 첫 턴이라면 
        if answer == -1:
            answer = total 
        else:
            answer = answer ^ total 
    
    return answer