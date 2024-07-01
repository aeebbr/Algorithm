'''
col = 2 라면, 각 튜플을 정렬하되, 두번째 컬럼이 커지는 순으로 정렬
=> lambda x: (x[col-1], -x[0])
'''

def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    # print(data)
    
    for i in range(row_begin-1, row_end):
        total = 0
        for j in range(len(data[i])):
            total += data[i][j] % (i+1)
        answer = answer ^ total
    
    return answer
    