'''
남은 수들을 최대한 적게 해야 
-> 큰 수들을 우선적으로 작은 수로 바꿔야
-> 매 턴마다 최댓값을 1 증감

0. 4, 3, 3
1. 3, 3, 3
2. 2, 3, 3
3. 2, 2, 3
4. 2, 2, 2

0. 2, 1, 2
1. 1, 1, 2

0. 1, 1
1. 0, 1
2. 0, 0 (최대값이 0이면 종료)
'''

import heapq
def solution(n, works):
    answer = 0
    q = []
    for w in works:
        heapq.heappush(q, (-w, w))
    
    while True:
        max = heapq.heappop(q)[1]
        if max == 0 or n == 0:
            heapq.heappush(q, (-max, max))
            break
        heapq.heappush(q, (-(max-1), max-1))
        n -= 1
    
    for i in q:
        answer += i[1] * i[1]
    
    return answer