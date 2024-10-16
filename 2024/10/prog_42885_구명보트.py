"""
큰 수 + 작은 수 
"""
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)

    while q:
        heavy = q.popleft()
        
        if not q:
            answer += 1
            break 
            
        light = q.pop()

        if heavy + light > limit:
            q.append(light)
            
        answer += 1
    
    return answer