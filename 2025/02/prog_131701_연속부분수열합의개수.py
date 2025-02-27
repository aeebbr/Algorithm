from collections import deque
def solution(elements):
    answer = []
    
    # 턴마다 수열 길이 제한하기 
    for limit in range(1, len(elements)):
        q = deque(maxlen = limit)
    
        # elements 두 번 돌리기 
        for e in elements * 2:
            q.append(e)
            answer.append(sum(q))
    
    # 모두 다 더한 값 추가 
    answer.append(sum(elements))
    
    return len(set(answer))