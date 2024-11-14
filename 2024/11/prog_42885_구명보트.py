from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))
    
    while q:
        answer += 1
        heavy = q.popleft()
        
        if not q:
            break
            
        light = q.pop()
        if heavy + light > limit: # 불가 
            q.append(light)
            
    return answer