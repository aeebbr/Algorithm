from collections import deque
def solution(elements):
    answer = []
    
    for limit in range(1, len(elements)):
        q = deque(maxlen = limit)
        
        # elements 두 번 돌리기 
        for e in elements * 2:
            q.append(e)
            answer.append(sum(q))
    
    answer.append(sum(elements))
    
    return len(set(answer))