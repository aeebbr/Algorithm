'''
곱이 최대가 되려면 각 수의 차이가 적여야 함
'''
import heapq

def solution(n, s):
    q = [(s//n)] * n
    heapq.heapify(q)
    total = sum(q)
    
    # 매 턴의 최솟값에 1씩 증가 
    while True:
        if total == s:
            break
        min = heapq.heappop(q)    
        heapq.heappush(q, min+1)
        total += 1

    q.sort()
    if q[0] == 0:
        return [-1]
    else:
        return q